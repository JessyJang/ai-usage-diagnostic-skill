#!/usr/bin/env python3
"""Offline structural checks only; NOT model/validity testing."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
main = (root / 'SKILL.md').read_text()
assert re.search(r'version: 2\.1\.0-beta\.1', main)
for file in ('references/scoring-protocol.md','references/output-contract.md','tests/validation-matrix.md','tests/run-log.csv','README.md','CHANGELOG.md'):
    assert (root / file).is_file(), file
for term in ('证据可信度','Red-team','复用运营','判断取舍','未知'):
    assert term.lower() in main.lower(), term
assert 'not a psychometrically validated test' in main
print('PASS: structure and required V2.1 sections; model execution NOT tested')
