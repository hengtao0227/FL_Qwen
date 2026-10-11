"""Operator-side preparation. A copied folder alone is not a sandbox."""
import argparse
import json
from pathlib import Path
from case_io import snapshot, digest, require, no_links


def prepare(inputs, case_id, destination):
    root = no_links(inputs)
    manifest_path = no_links(root/'manifest.json')
    manifest = json.loads(manifest_path.read_bytes())
    rows = [r for r in manifest['cases'] if r['case_id'] == case_id]
    require(len(rows) == 1, 'Case not in manifest')
    data = snapshot(root/'cases'/case_id)
    row = rows[0]
    require({n:digest(b) for n,b in data.items()} == row['files_sha256'],
            'Case differs from trusted release manifest')
    destination = Path(destination).absolute()
    require(not destination.is_relative_to(root), 'Output must be outside the release inputs')
    require(not destination.exists(), 'Destination must be new')
    require(destination.parent.exists(), 'Create the parent directory first')
    no_links(destination.parent)
    destination.mkdir()
    for name, content in data.items():
        (destination/name).write_bytes(content)
    snapshot(destination)
    return {'case_id':case_id,'files':len(data),'prepared':str(destination),
            'host_isolation_verified':False}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs',type=Path,required=True)
    p.add_argument('--case',required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    print(json.dumps(prepare(a.inputs,a.case,a.out),ensure_ascii=False,indent=2))
