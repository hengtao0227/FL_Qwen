"""Prepare every classic case using a fixed snapshot and the official source patch.

No legacy AutoFL method lists or coverage selections are used. All declared
production methods are extracted by the same tree-sitter implementation.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib
import json
import subprocess
import threading
import zipfile
import collect_sources as sources
import extract_java as extraction

REPOS={'Chart':'jfreechart','Closure':'closure-compiler.git','Lang':'commons-lang.git',
       'Math':'commons-math.git','Mockito':'mockito.git','Time':'joda-time.git'}
PROJECTS={'Chart':26,'Closure':133,'Lang':65,'Math':106,'Mockito':38,'Time':27}
EXTRACT_LOCK=threading.Lock()

def prepare(cid,args):
    project=cid.split('_')[0]
    row=sources.metadata(cid); rev=row['revision.id.fixed']
    archive=args.cache/'archives'/f'{project}-{rev}.zip'
    archive.parent.mkdir(parents=True,exist_ok=True)
    if not archive.exists():
        tmp=archive.with_suffix('.part.zip')
        if project=='Chart':
            command=[str(args.jdk/'bin/java.exe'),'-cp',str(args.svnkit/'*')+';'+str(args.svnkit),
                     'SvnSnapshot',str(args.repos/REPOS[project]),rev,str(tmp)]
        else:
            command=['git','--git-dir='+str(args.repos/REPOS[project]),'archive',
                     '--format=zip','--prefix=snapshot/','--output='+str(tmp),rev]
        p=subprocess.run(command,capture_output=True,text=True,timeout=240)
        if p.returncode:raise RuntimeError(p.stderr[-3000:])
        with zipfile.ZipFile(tmp) as z:
            if z.testzip() is not None:raise RuntimeError('Invalid source archive')
        tmp.replace(archive)
    audit=sources.reconstruct((cid,archive,'https://defects4j.org/downloads/defects4j-repos-v3.zip',row))
    # One shared parser is deliberately serialized; source export remains concurrent.
    audit_path=args.cache/'source_audit'/f'{cid}.extraction.json'
    if not audit_path.exists():
        with EXTRACT_LOCK: result=extraction.collect(cid)
    else: result=json.loads(audit_path.read_bytes())
    if result['production_parse_errors']:
        raise ValueError('Production parse errors: '+str(result['production_parse_errors'][:3]))
    print('PREPARED',cid,result['method_count'],flush=True)
    return cid

def main():
    p=argparse.ArgumentParser()
    for name in ('cache','d4j','repos','jdk','svnkit'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--cases',nargs='*');p.add_argument('--workers',type=int,default=4)
    args=p.parse_args()
    sources.CACHE=extraction.CACHE=args.cache.resolve()
    sources.D4J=extraction.D4J=args.d4j.resolve()/'framework/projects'
    cases=args.cases or [f'{p}_{i}' for p,n in PROJECTS.items() for i in range(1,n+1)]
    # Shared fixed revisions must not be exported concurrently.
    groups={}
    for cid in cases:groups.setdefault((cid.split('_')[0],sources.metadata(cid)['revision.id.fixed']),[]).append(cid)
    errors=[]
    def group_run(group):
        result=[]
        for cid in group:
            try:prepare(cid,args)
            except Exception as e:
                result.append({'case_id':cid,'error':str(e)})
                print('PREPARE_FAILED',cid,str(e),flush=True)
        return result
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for future in as_completed([pool.submit(group_run,g) for g in groups.values()]):errors.extend(future.result())
    args.cache.mkdir(parents=True,exist_ok=True)
    (args.cache/'preparation_errors.json').write_text(json.dumps(errors,indent=2),encoding='utf8')
    (args.cache/'preparation_complete.json').write_text(json.dumps({'cases':cases,'errors':errors}),encoding='utf8')
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
