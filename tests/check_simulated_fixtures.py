import json
from pathlib import Path
items=json.loads((Path(__file__).parent/'synthetic-fixtures.json').read_text())
assert len(items)==22
assert [x['id'] for x in items]==[f'T{i:02d}' for i in range(1,23)]
assert all(x['synthetic_input'] and x['expected_invariant'] and x['status']=='NOT_EXECUTED_AGAINST_MODEL' for x in items)
assert len({x['synthetic_input'] for x in items})==22
print('PASS: 22/22 synthetic fixture integrity checks (NOT model-evaluation results)')
