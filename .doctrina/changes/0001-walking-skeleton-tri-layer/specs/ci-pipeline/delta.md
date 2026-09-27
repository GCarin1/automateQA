# Spec Delta — capability: ci-pipeline

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/ci-pipeline/spec.md`

---

```ops
set-header Status: active
set-header Implementation: implemented — green run not yet observed (`.github/workflows/tests.yml`)
bump-version minor
replace-requirement ubiquitous 2: The workflow shall run a secret scan, lint, the template's framework checks and the example suite, in that order.
```
