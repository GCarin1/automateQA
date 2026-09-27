# Spec — project-structure

**Capability:** project-structure
**Status:** active
**Implementation:** verified — tri-layer walking skeleton (`tests/framework/test_layers.py`)
**Realizes:** SC2, SC3
**Last updated:** 2026-09-27
**Version:** 0.2.0

## Purpose

Define the layered folder layout of the template and the single responsibility of each folder, following the test automation framework layers of ISTQB CTAL-TAE v2.0 §3.1.3 (ADR 0005): test scripts, business logic (page objects and the flow model of §3.1.5) and core libraries independent of the system under test. The layout is what adopters copy; it must be obvious, documented and enforced.

## Requirements (EARS)

### Ubiquitous

- The template shall organise test code in the three test automation framework layers of ISTQB CTAL-TAE v2.0 §3.1.3: `tests/e2e/` (test scripts), `business/` (business logic: `pages/`, `flows/`, `data/`, `fixtures.py`) and `core/` (core libraries independent of the SUT).
- The template shall document, in one README section, the responsibility of every top-level folder and the CTAL-TAE layer it maps to.
- The template shall allow dependencies only downward: test scripts → business logic → core libraries.

### Event-driven

- When a contributor adds a new page, the template shall require only a new module under `business/pages/` and no edit to `core/`.

### Unwanted-behavior (must-not)

- The template shall not import `core` or the automation driver package from any module under `tests/e2e/`, nor the driver package from `business/flows/`.
- The template shall not place locators outside `business/pages/`.
- The template shall not place assertions inside `business/` or `core/`.
- The template shall not import `business` or `tests` from any module under `core/`.

### Optional

- Where an adopter needs API or mobile tests, the template may host them as sibling folders under `tests/` with their adapters in `business/`, reusing `core/`.

## Acceptance criteria

1. [verified] An automated check fails when a test script imports core or the driver package, or a flow imports the driver package — verified by `tests/framework/test_layers.py`.
2. [verified] The README folder table lists every top-level folder and maps each layer folder to its CTAL-TAE layer — verified by `tests/framework/test_docs.py`.
3. [verified] An automated check fails when an assert statement appears under business/ or core/ — verified by `tests/framework/test_layers.py`.
4. [verified] An automated check fails when a locator call appears in test scripts, flows or test data — verified by `tests/framework/test_layers.py`.
5. [verified] An automated check fails when core/ imports business or tests — verified by `tests/framework/test_layers.py`.

## Maturity

**MVP (committed):**

- Three-layer layout (`tests/e2e/`, `business/`, `core/`), README folder table, automated layer checks.

**Future (aspirational, not committed):**

- Cookiecutter/Copier generator that scaffolds the layout into an empty repository.
- `business/components/` for widgets reused across pages, and adapters for API (`business/clients/`) and mobile.

## Out of scope for this spec

- The choice of runner and driver (see ADRs).
- Test naming and writing style (see `test-authoring`).
