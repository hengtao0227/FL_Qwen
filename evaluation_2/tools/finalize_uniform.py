"""Wait for verified collection, then assemble and validate the complete release."""
import json
from pathlib import Path
import subprocess
import sys
import time

root=Path(__file__).resolve().parents[2]
runs=Path('D:/codex_uniform395/runs')
while True:
    try: status=json.loads((runs/'collection_status.json').read_bytes())
    except (OSError,ValueError):time.sleep(5);continue
    if status['requested']==395 and not status['pending'] and not status['active']:
        if status['failed'] or status['passed']!=395:
            raise SystemExit('Collection incomplete: '+str({k:v for k,v in status.items() if k!='results'}))
        break
    time.sleep(5)

commands=[
    [sys.executable,'evaluation_2/tools/assemble_uniform.py','--cache','D:/codex_uniform395/cache',
     '--d4j','${USER_HOME}/Desktop/defects4j-master/defects4j-master','--coverage',str(runs)],
    [sys.executable,'evaluation_2/tools/validate_release.py'],
    [sys.executable,'evaluation_2/tools/report_uniform.py'],
]
for command in commands:
    print('RUNNING',command[1],flush=True)
    subprocess.run(command,cwd=root,check=True)
