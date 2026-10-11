"""Operator-only official fixed-to-buggy patch mapping. Configure D4J before use."""
import re
import hashlib
from pathlib import Path
D4J = None
def sha(data): return hashlib.sha256(data).hexdigest()

def patch_changes(path):
    """Read target (buggy) line positions of exact official patch edits.

    Deleted fixed lines are insertion gaps on the buggy side, only mapped when
    both adjacent buggy lines are inside the SAME method. External edits remain
    explicitly unmapped; no nearest-method guessing is used.
    """
    raw=path.read_bytes()
    try: source=raw.decode('utf-8-sig')
    except UnicodeDecodeError: source=raw.decode('latin-1')
    lines=source.splitlines();changes=[]
    current=None;i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('+++ '):current=line[4:].split('\t')[0].removeprefix('b/')
        match=re.match(r'@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@',line)
        if not match:i+=1;continue
        new=int(match[1]);i+=1
        while i<len(lines) and not lines[i].startswith(('@@','diff --git','--- ')):
            line=lines[i]
            if not line or line[0] not in ' +-\\':break
            if line.startswith(' '):new+=1;i+=1;continue
            if line.startswith('\\'):i+=1;continue
            start=new;added=[];deleted=[]
            while i<len(lines) and lines[i].startswith(('+','-')) and not lines[i].startswith(('+++ ','--- ')):
                if lines[i][0]=='+':added.append(new);new+=1
                else:deleted.append(lines[i][1:])
                i+=1
            if added:
                changes.extend(dict(src_path=current,kind='buggy_line',line=n) for n in added)
            elif deleted:
                changes.append(dict(src_path=current,kind='insertion_gap',before_line=start-1,after_line=start))
        # The next iteration handles the next hunk or file header.
    return changes

def label_case(cid,index):
    project,bid=cid.split('_');patch=D4J/project/'patches'/f'{bid}.src.patch'
    changes=patch_changes(patch);selected={};unmapped=[];mapped=[]
    for change in changes:
        candidates=[]
        for method in index:
            if method['src_path']!=change['src_path']:continue
            a,b=method['begin_line'],method['end_line']
            if change['kind']=='buggy_line':inside=a<=change['line']<=b
            else:inside=a<=change['before_line'] and change['after_line']<=b
            if inside:candidates.append(method)
        if candidates:
            # A nested anonymous-class method is distinct from its enclosing method.
            size=min(m['end_line']-m['begin_line'] for m in candidates)
            hits=[m for m in candidates if m['end_line']-m['begin_line']==size]
            for m in hits:selected[m['candidate_id']]=m
            mapped.append({**change,'candidate_ids':[m['candidate_id'] for m in hits]})
        else:unmapped.append(change)
    refs=[{k:m[k] for k in ('candidate_id','signature','src_path','begin_line','end_line')}
          for m in selected.values()]
    return refs,dict(case_id=cid,reference_source='official_patch_to_static_method',
        patch_sha256=sha(patch.read_bytes()),mapped_changes=mapped,unmapped_changes=unmapped,
        mapping_policy='changed buggy lines; deleted fixed-code gaps require both adjacent lines in same method; smallest containing method',
        limitations='Patch-derived reference methods, not an independent semantic oracle. Non-method edits remain unmapped.')


