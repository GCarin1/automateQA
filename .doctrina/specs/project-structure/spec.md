# Spec — project-structure

**Capability:** project-structure
**Status:** draft
**Implementation:** planned
**Realizes:** SC2, SC3
**Last updated:** 2026-09-27
**Version:** 0.1.0

## Purpose

Define the layered folder layout of the template and the single responsibility of each folder, mapped to the layers of the ISTQB generic Test Automation Architecture (gTAA): test definition (tests), business flows, test adaptation (pages/components) and a core that wraps the automation driver. The layout is what adopters copy; it must be obvious, documented and enforced.

## Requirements (EARS)

### Ubiquitous

- The template shall organise test code in four layers: `tests/` (test definition), `flows/` (business tasks composed of page actions), `pages/` with `components/` (test adaptation: locators and UI interactions) and `core/` (driver lifecycle, configuration loading, evidence capture).
- The template shall document, in one README section, the responsibility of every top-level folder and the gTAA layer it maps to.
- The template shall allow dependencies only downward: tests → flows → pages/components → core.

### Event-driven

- When a contributor adds a new page, the template shall require only a new module under `pages/` and no edit to `core/`.

### Unwanted-behavior (must-not)

- The template shall not import the automation driver package from any module under `tests/` or `flows/`.
- The template shall not place locators outside `pages/` and `components/`.
- The template shall not place assertions inside `pages/`, `components/` or `core/`.

### Optional

- Where an adopter needs API or mobile tests, the template may host them as sibling folders under `tests/` reusing `core/`.

## Acceptance criteria

1. [unverified] An automated architecture check fails when a module under tests/ or flows/ imports the driver package — verified by `tests/architecture/test_layers.py`.
2. [unverified] The README contains a folder table listing every top-level folder with its gTAA layer — verified by `tests/architecture/test_readme_structure.py`.
3. [unverified] An automated check fails when an assert statement appears under pages/, components/ or core/ — verified by `tests/architecture/test_layers.py`.

## Maturity

**MVP (committed):**

- Four-layer layout, README folder table, import-direction check.

**Future (aspirational, not committed):**

- Cookiecutter/Copier generator that scaffolds the layout into an empty repository.
- Additional layers for API (`clients/`) and mobile.

## Out of scope for this spec

- The choice of runner and driver (see ADRs).
- Test naming and writing style (see `test-authoring`).
