"""Collect the same method-entry evidence for all six projects, with restart support."""
import argparse
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from pathlib import Path
import json
import time
import traceback
from collect_method_coverage import setup_agent, collect
from coverage_selection import select_covered
from case_io import digest

PROJECTS={'Chart':26,'Closure':133,'Lang':65,'Math':106,'Mockito':38,'Time':27}

def main():
    p=argparse.ArgumentParser()
    for key in ('cache','d4j','jdk','jdk7','runtime','runs'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--cases',nargs='*');p.add_argument('--workers',type=int,default=4)
    p.add_argument('--watch',action='store_true');p.add_argument('--force',action='store_true')
    a=p.parse_args()
    for key in ('cache','d4j','jdk','jdk7','runtime','runs'):setattr(a,key,getattr(a,key).resolve())
    cases=a.cases or [f'{p}_{i}' for p,n in PROJECTS.items() for i in range(1,n+1)]
    a.runtime.mkdir(parents=True,exist_ok=True);a.runs.mkdir(parents=True,exist_ok=True)
    agent,junit=setup_agent(a.jdk,a.d4j,a.runtime)
    agent_hash=digest(agent.read_bytes())
    results={};waiting=set(cases)
    def process(cid):
        try:
            dest=a.runs/cid/'coverage.json'
            compatible=dest.exists() and json.loads(dest.read_bytes()).get('agent_sha256')==agent_hash
            if compatible and not a.force:
                _,audit=select_covered(cid,a.cache/'raw_extracted'/cid,a.runs)
                print('REUSED_VERIFIED',cid,audit['covered_candidate_count'],flush=True)
            else:
                if dest.exists():dest.unlink()
                collect(cid,a.cache,a.d4j,a.jdk,a.jdk7,a.runtime,a.runs,None,agent,junit)
                _,audit=select_covered(cid,a.cache/'raw_extracted'/cid,a.runs)
            return {'case_id':cid,'status':'passed','candidate_count':audit['covered_candidate_count']}
        except Exception as e:
            log=a.runs/cid/'collection_error.txt';log.parent.mkdir(parents=True,exist_ok=True)
            log.write_text(traceback.format_exc(),encoding='utf8')
            print('FAILED',cid,str(e),flush=True)
            return {'case_id':cid,'status':'failed','error':str(e)}
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        active={}
        while waiting or active:
            for cid in cases:
                if len(active)>=a.workers:break
                if cid not in waiting:continue
                audit=a.cache/'source_audit'/f'{cid}.extraction.json'
                if not audit.exists():continue
                if json.loads(audit.read_bytes())['production_parse_errors']:
                    results[cid]={'case_id':cid,'status':'failed','error':'Production parse errors'};waiting.remove(cid);continue
                waiting.remove(cid);active[pool.submit(process,cid)]=cid
                print('STARTED',cid,flush=True)
            if not active:
                if waiting:
                    complete=a.cache/'preparation_complete.json'
                    info=json.loads(complete.read_bytes()) if complete.exists() else {}
                    if not a.watch or set(cases)<=set(info.get('cases',[])):
                        for cid in waiting:results[cid]={'case_id':cid,'status':'failed','error':'Sources not ready'}
                        waiting.clear();break
                    time.sleep(5)
                continue
            done,_=wait(active,timeout=5,return_when=FIRST_COMPLETED)
            for f in done:
                cid=active.pop(f);results[cid]=f.result()
            status={'requested':len(cases),'passed':sum(r['status']=='passed' for r in results.values()),
                    'failed':sum(r['status']=='failed' for r in results.values()),'pending':len(waiting),
                    'active':list(active.values()),'results':results}
            tmp=a.runs/'collection_status.tmp';tmp.write_text(json.dumps(status,indent=2),encoding='utf8')
            for attempt in range(30):
                try:
                    tmp.replace(a.runs/'collection_status.json');break
                except PermissionError:
                    if attempt==29:raise
                    time.sleep(0.1)
    errors=[r for r in results.values() if r['status']=='failed']
    status={'requested':len(cases),'passed':len(results)-len(errors),'failed':len(errors),
            'pending':0,'active':[],'results':results}
    (a.runs/'collection_status.json').write_text(json.dumps(status,indent=2),encoding='utf8')
    (a.runs/'last_collection_errors.json').write_text(json.dumps(errors,indent=2),encoding='utf8')
    print('COLLECTION_FINISHED',len(results),'failed',len(errors),flush=True)
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
