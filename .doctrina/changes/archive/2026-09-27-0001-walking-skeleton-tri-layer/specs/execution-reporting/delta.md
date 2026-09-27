# Spec Delta — capability: execution-reporting

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/execution-reporting/spec.md`

---

```ops
set-header Status: active
set-header Implementation: verified — pytest addopts (`pyproject.toml`)
bump-version minor
replace-criterion 1: [verified] A deliberately failing UI test leaves a screenshot and a trace in the output folder — verified by `tests/framework/test_evidence.py`.
replace-criterion 2: [verified] A run writes junit.xml and report.html with the configured report options — verified by `tests/framework/test_reports.py`.
replace-criterion 3: [verified] An unknown marker makes the run fail at collection — verified by `tests/framework/test_markers.py`.
append-criterion [verified] A run that collects zero tests exits non-zero — verified by `tests/framework/test_reports.py`.
```
