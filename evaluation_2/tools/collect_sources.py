"""Collect exact fixed snapshots and apply official fixed-to-buggy patches.

This is an operator tool. Its cache and patches must never be supplied to the
localization agent. No tests are executed by this static material collector.
"""
import concurrent.futures
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import time
import zipfile
import requests
import re

def patch_strip(path):
    header=re.search(r'^--- ([^\t\n]+)',path.read_text(encoding='utf-8',errors='replace'),re.M)[1]
    return '-p1' if header.startswith('a/') else '-p0'

ROOT = Path(__file__).resolve().parents[1]
D4J = ROOT / 'defects4j-master/framework/projects'
CACHE = ROOT / 'dataset395_cache'
PROJECTS = {'Chart':26, 'Closure':133, 'Lang':65, 'Math':106, 'Mockito':38, 'Time':27}
REPOS = {'Mockito':'mockito/mockito', 'Closure':'google/closure-compiler',
         'Lang':'apache/commons-lang', 'Time':'JodaOrg/joda-time'}
MISSING = ['Closure_63','Closure_93','Lang_2', *[f'Mockito_{i}' for i in range(1,39)], 'Time_21']

def metadata(cid):
    project, bid = cid.split('_')
    records = []
    for name in ('active-bugs.csv', 'deprecated-bugs.csv'):
        with (D4J/project/name).open(encoding='utf-8-sig', newline='') as f:
            records.extend(csv.DictReader(f))
    return next(r for r in records if r['bug.id'] == bid)

def download(cid):
    project, bid = cid.split('_')
    row = metadata(cid)
    rev = row['revision.id.fixed']
    url = f'https://codeload.github.com/{REPOS[project]}/zip/{rev}'
    archive = CACHE/'archives'/f'{project}-{rev}.zip'
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        for attempt in range(4):
            try:
                r = requests.get(url, timeout=(25,180)); r.raise_for_status()
                # Validate before accepting the cache entry.
                import io
                with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                    assert z.testzip() is None
                tmp = archive.with_suffix('.tmp')
                tmp.write_bytes(r.content); tmp.replace(archive)
                break
            except Exception:
                if attempt == 3: raise
                time.sleep(2 + attempt)
    return cid, archive, url, row

def reconstruct(item):
    cid, archive, url, row = item
    project, bid = cid.split('_')
    out = CACHE/'buggy_sources'/cid
    audit = CACHE/'source_audit'/f'{cid}.json'
    if audit.exists():
        return json.loads(audit.read_text(encoding='utf-8'))
    out.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            parts = Path(info.filename).parts[1:]
            if project=='Time' and parts and parts[0]=='JodaTime': parts=parts[1:]
            if not parts or info.is_dir(): continue
            relative = Path(*parts)
            # Only Java sources are needed for offline extraction.
            if relative.suffix != '.java': continue
            target = (out/relative).resolve()
            assert target.is_relative_to(out.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(info))
    patch = D4J/project/'patches'/f'{bid}.src.patch'
    adaptations=[]
    if cid=='Lang_48':
        hook=D4J/project/'compile-errors/test-44-48.diff'
        r=subprocess.run(['git','apply','--no-index',patch_strip(hook),str(hook)],cwd=out,capture_output=True,text=True)
        if r.returncode:raise RuntimeError(cid+': official pre-checkout hook failed: '+r.stderr)
        adaptations.append({'official_hook':str(hook),'sha256':hashlib.sha256(hook.read_bytes()).hexdigest()})
    # Run outside the parent git repository and require exact context matching.
    for args in (['--check'], []):
        r = subprocess.run(['git','apply','--no-index',patch_strip(patch),'--whitespace=nowarn',*args,str(patch)],
                           cwd=out, capture_output=True, text=True)
        if r.returncode: raise RuntimeError(cid+': '+r.stderr)
    result = {'case_id':cid,'source_url':url,'revision_fixed':row['revision.id.fixed'],
        'revision_buggy_upstream':row['revision.id.buggy'],
        'construction':'official fixed snapshot plus official fixed-to-buggy src.patch',
        'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'patch_sha256':hashlib.sha256(patch.read_bytes()).hexdigest(),
        'deprecated_version':row.get('deprecated.version'),
        'deprecated_reason':row.get('deprecated.reason'),
        'runtime_tests_executed':False,
        'source_adaptations':adaptations,
        'limitations':'Static source reconstruction; build/dependency/test-runner post-checkout hooks are not executed.'}
    audit.parent.mkdir(parents=True, exist_ok=True)
    audit.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
    return result

def main():
    errors=[]
    # Some cases share a fixed revision. Download each archive once.
    unique={}
    for cid in MISSING:
        p=cid.split('_')[0]; key=(p,metadata(cid)['revision.id.fixed'])
        unique.setdefault(key,cid)
    downloaded={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        pending={pool.submit(download,cid):key for key,cid in unique.items()}
        for future in concurrent.futures.as_completed(pending):
            key=pending[future]
            try:
                item=future.result(); downloaded[key]=item
                print('DOWNLOADED',item[0],item[1].stat().st_size,flush=True)
            except Exception as e:
                errors.append({'key':key,'error':str(e)}); print('ERROR',key,str(e),flush=True)
    for cid in MISSING:
        p=cid.split('_')[0]; row=metadata(cid); key=(p,row['revision.id.fixed'])
        if key not in downloaded: continue
        _,archive,url,_=downloaded[key]
        try:
            reconstruct((cid,archive,url,row)); print('RECONSTRUCTED',cid,flush=True)
        except Exception as e:
            errors.append({'case_id':cid,'error':str(e)});print('ERROR',cid,str(e),flush=True)
    (CACHE/'collection_errors.json').write_text(json.dumps(errors,indent=2),encoding='utf-8')
    if errors: raise SystemExit(1)

if __name__=='__main__': main()
