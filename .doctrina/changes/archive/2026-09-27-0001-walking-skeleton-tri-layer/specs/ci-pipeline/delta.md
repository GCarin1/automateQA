# Spec Delta — capability: ci-pipeline

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/ci-pipeline/spec.md`

---

```ops
set-header Status: active
set-header Implementation: verified — GitHub Actions runs 36293277897 (red, artifacts uploaded) and 36293369635 (green) (`.github/workflows/tests.yml`)
bump-version minor
replace-requirement ubiquitous 2: The workflow shall run a secret scan, lint, the template's framework checks and the example suite, in that order.
replace-criterion 1: [verified] The workflow runs green on push; observed on the change branch in run 36293369635 — verified by `.github/workflows/tests.yml`.
replace-criterion 2: [verified] A failing test makes the workflow job fail and still uploads artifacts/; observed in run 36293277897 — verified by `.github/workflows/tests.yml`.
```
