# Spec Delta — capability: project-structure

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/project-structure/spec.md`

---

Manual merge (prose): Purpose, Maturity and Out of scope rewritten to the
Tri-Layer vocabulary of ADR 0005 (three layers, flow model, no `components/`
folder in the MVP).

```ops
set-header Status: active
set-header Implementation: verified — tri-layer walking skeleton (`tests/framework/test_layers.py`)
bump-version minor
replace-requirement ubiquitous 1: The template shall organise test code in the three test automation framework layers of ISTQB CTAL-TAE v2.0 §3.1.3: `tests/e2e/` (test scripts), `business/` (business logic: `pages/`, `flows/`, `data/`, `fixtures.py`) and `core/` (core libraries independent of the SUT).
replace-requirement ubiquitous 2: The template shall document, in one README section, the responsibility of every top-level folder and the CTAL-TAE layer it maps to.
replace-requirement ubiquitous 3: The template shall allow dependencies only downward: test scripts → business logic → core libraries.
replace-requirement event 1: When a contributor adds a new page, the template shall require only a new module under `business/pages/` and no edit to `core/`.
replace-requirement unwanted 1: The template shall not import `core` or the automation driver package from any module under `tests/e2e/`, nor the driver package from `business/flows/`.
replace-requirement unwanted 2: The template shall not place locators outside `business/pages/`.
replace-requirement unwanted 3: The template shall not place assertions inside `business/` or `core/`.
append-requirement unwanted: The template shall not import `business` or `tests` from any module under `core/`.
replace-requirement optional 1: Where an adopter needs API or mobile tests, the template may host them as sibling folders under `tests/` with their adapters in `business/`, reusing `core/`.
replace-criterion 1: [verified] An automated check fails when a test script imports core or the driver package, or a flow imports the driver package — verified by `tests/framework/test_layers.py`.
replace-criterion 2: [verified] The README folder table lists every top-level folder and maps each layer folder to its CTAL-TAE layer — verified by `tests/framework/test_docs.py`.
replace-criterion 3: [verified] An automated check fails when an assert statement appears under business/ or core/ — verified by `tests/framework/test_layers.py`.
append-criterion [verified] An automated check fails when a locator call appears in test scripts, flows or test data — verified by `tests/framework/test_layers.py`.
append-criterion [verified] An automated check fails when core/ imports business or tests — verified by `tests/framework/test_layers.py`.
```
