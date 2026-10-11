"""Static Java extraction. Reads buggy Java and trigger logs only, never patches.

All declared production methods/constructors are candidates, including anonymous
classes and bodyless declarations. No coverage or relevance filtering is applied.
"""
import json
from pathlib import Path
import re
from tree_sitter import Language, Parser
import tree_sitter_java
from collect_sources import CACHE, D4J, MISSING

CLASSES={'class_declaration','interface_declaration','enum_declaration',
         'annotation_type_declaration','record_declaration'}
METHODS={'method_declaration','constructor_declaration','compact_constructor_declaration',
         'annotation_type_element_declaration'}
PARSER=Parser(Language(tree_sitter_java.language()))

def text(node,data):
    return data[node.start_byte:node.end_byte].decode('utf-8') if node else ''

def walk(node):
    yield node
    for child in node.named_children: yield from walk(child)

def extract(path,relative):
    # Source archives occasionally contain Latin-1 comments.
    raw=path.read_bytes()
    try: source=raw.decode('utf-8-sig'); encoding='utf-8'
    except UnicodeDecodeError: source=raw.decode('latin-1'); encoding='latin-1'
    data=source.encode('utf-8'); lines=source.splitlines()
    tree=PARSER.parse(data)
    package=next((text(n,data).removeprefix('package').strip().rstrip(';').strip()
                  for n in tree.root_node.named_children if n.type=='package_declaration'),'')
    methods=[];fields=[];class_rows=[]
    def class_name(node):
        names=[];parent=node.parent
        while parent:
            if parent.type in CLASSES:
                names.append(text(parent.child_by_field_name('name'),data))
            elif parent.type=='class_body' and parent.parent and parent.parent.type in (
                    'object_creation_expression','enum_constant'):
                names.append('anonymous_L'+str(parent.start_point.row+1))
            parent=parent.parent
        return '.'.join(([package] if package else [])+list(reversed(names)))
    for node in walk(tree.root_node):
        if node.type in CLASSES:
            name=class_name(node)+'.'+text(node.child_by_field_name('name'),data)
            superclass=node.child_by_field_name('superclass')
            class_rows.append({'name':name.lstrip('.'),'superclass':text(superclass,data).removeprefix('extends').strip()})
        if node.type not in METHODS|{'field_declaration','constant_declaration'}: continue
        cls=class_name(node)
        name=text(node.child_by_field_name('name'),data)
        params=node.child_by_field_name('parameters')
        types=[]
        if params:
            for p in params.named_children:
                if p.type not in ('formal_parameter','spread_parameter','receiver_parameter'): continue
                typ=text(p.child_by_field_name('type'),data)
                if not typ:
                    typ=next((text(c,data) for c in p.named_children
                              if c.type not in ('modifiers','variable_declarator','identifier')),'?')
                dims=p.child_by_field_name('dimensions')
                typ+=text(dims,data)
                types.append(typ+('...' if p.type=='spread_parameter' else ''))
        prev=node.prev_named_sibling
        comment=text(prev,data) if prev and prev.type in ('block_comment','line_comment') else ''
        begin=node.start_point.row+1;end=node.end_point.row+1
        signature=cls+'.'+name+'('+','.join(types)+')'
        if node.type in ('field_declaration','constant_declaration'):
            names=[text(c.child_by_field_name('name'),data) for c in node.named_children
                   if c.type=='variable_declarator']
            signature=cls+'.'+','.join(names)
        row=dict(class_name=cls,src_path=relative,signature=signature,
                 begin_line=begin,end_line=end,comment=comment,
                 snippet='\n'.join(lines[begin-1:end]))
        (methods if node.type in METHODS else fields).append(row)
    errors=[{'line':n.start_point.row+1,'type':n.type,'text':text(n,data)[:120]}
            for n in walk(tree.root_node) if n.type=='ERROR' or n.is_missing]
    return methods,fields,class_rows,errors,encoding

def production_root(cid,root):
    project=cid.split('_')[0]
    if project=='Mockito': options=['src/main/java','src']
    elif project=='Closure': options=['src']
    elif project=='Lang': options=['src/main/java','src/java']
    elif project=='Time': options=['src/main/java','src/java']
    elif project=='Math': options=['src/main/java','src/java']
    elif project=='Chart': options=['source']
    return next(root/p for p in options if (root/p).is_dir())

def collect(cid):
    root=CACHE/'buggy_sources'/cid; prod=production_root(cid,root)
    methods=[];fields=[];tests=[];classes=[];errors=[];encodings={}
    for path in sorted(root.rglob('*.java')):
        relative=path.relative_to(root).as_posix()
        if cid.startswith('Time_') and relative.startswith('JodaTime/') and (root/'src').is_dir():continue
        m,f,c,e,encoding=extract(path,relative)
        is_prod=path.is_relative_to(prod)
        # src is the legacy production root; test folders are siblings.
        if is_prod:
            methods.extend(m);fields.extend(f)
            errors.extend({'file':relative,**x} for x in e)
        else: tests.extend(m)
        classes.extend(c)
        if encoding!='utf-8': encodings[relative]=encoding
    class_map={c['name']:c['superclass'] for c in classes}
    def ancestors(cls):
        seen=set()
        while cls in class_map and class_map[cls]:
            sup=re.sub(r'<.*>','',class_map[cls]).strip()
            possible=[c for c in class_map if c==sup or c.endswith('.'+sup)]
            same=[c for c in possible if c.rsplit('.',1)[0]==cls.rsplit('.',1)[0]]
            possible=same or possible
            if len(possible)!=1 or possible[0] in seen: break
            cls=possible[0];seen.add(cls);yield cls
    children_map={}
    for c in class_map:
        for ancestor in ancestors(c): children_map.setdefault(ancestor,[]).append(c)
    for t in tests:
        children=children_map.get(t['class_name'],[])
        if children:t['child_classes']=children
    assert methods and tests,(cid,len(methods),len(tests))
    dest=CACHE/'raw_extracted'/cid;dest.mkdir(parents=True,exist_ok=True)
    for name,value in [('snippet.json',methods),('field_snippet.json',fields),('test_snippet.json',tests)]:
        (dest/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    project,bid=cid.split('_')
    (dest/'failing_tests').write_bytes((D4J/project/'trigger_tests'/bid).read_bytes())
    audit=dict(case_id=cid,candidate_scope='all_declared_production_methods_and_constructors',
               production_root=prod.relative_to(root).as_posix(),method_count=len(methods),
               production_parse_errors=errors,non_utf8_files=encodings)
    (CACHE/'source_audit'/f'{cid}.extraction.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
    print('EXTRACTED',cid,len(methods),'parse_errors',len(errors),flush=True)
    return audit

if __name__=='__main__':
    for cid in MISSING: collect(cid)
