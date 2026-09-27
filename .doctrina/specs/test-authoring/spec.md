# Spec — test-authoring

**Capability:** test-authoring
**Status:** active
**Implementation:** verified — rules R1–R10 (`docs/writing-tests.md`)
**Realizes:** SC2, SC3
**Depends on:** project-structure
**Last updated:** 2026-09-27
**Version:** 0.2.0

## Purpose

Define how a test is written in the template so any two tests written by different people look the same: naming, structure, locator strategy, waiting strategy and data handling. These rules are the clean-code core of the standard.

## Requirements (EARS)

### Ubiquitous

- Each test shall follow the Arrange-Act-Assert structure, and each test shall verify one behaviour.
- Each test shall be named `test_<behaviour>_<expected_result>` and live in a module named after the feature it covers.
- Page objects shall expose intention-revealing methods (for example `sign_in(name, password)`) and return page objects or values, never raw driver elements.
- Locators shall follow the priority: accessible role/label → test id attribute (`data-testid`) → CSS selector; XPath is allowed only with a comment justifying it.
- Test data shall come from fixtures or factories, never from literals repeated across tests.
- Assertions shall be made only in test scripts, on values returned by pages and flows.

### Event-driven

- When an element is not ready, the interaction shall wait explicitly on a condition with a bounded timeout declared in configuration.
- When a wait times out, the interaction shall raise an error naming the locator and the timeout.

### Unwanted-behavior (must-not)

- The template shall not use fixed sleeps (`time.sleep`) in `core/`, `business/` or `tests/`.
- The template shall not catch and silently discard exceptions raised by interactions.
- A test shall not depend on the execution order or state left by another test.

### Optional

- Where a team adopts BDD, the template may bind Gherkin feature files to the same flows through pytest-bdd, keeping step definitions free of locators.

## Acceptance criteria

1. [verified] A static check fails the build when a fixed sleep appears under core/, business/ or tests/ — verified by `tests/framework/test_conventions.py`.
2. [verified] A static check fails the build when a bare except or an except block containing only pass appears in the template code — verified by `tests/framework/test_conventions.py`.
3. [verified] The example suite runs green in random order — verified by `tests/e2e/test_login.py`.
4. [verified] The guide docs/writing-tests.md documents rules R1 to R10, each with a correct and an incorrect example — verified by `tests/framework/test_docs.py`.
5. [verified] A wait timeout raises an error that names the locator and the timeout — verified by `tests/framework/test_base_page.py`.
6. [verified] A static check fails the build when a test name does not follow test_<behaviour>_<expected_result> — verified by `tests/framework/test_conventions.py`.

## Maturity

**MVP (committed):**

- AAA, naming, locator priority, explicit waits, no sleeps, no swallowed exceptions, writing guide.

**Future (aspirational, not committed):**

- Optional BDD module (pytest-bdd) with one example feature.
- Linter plugin enforcing the rules instead of ad-hoc checks.

## Out of scope for this spec

- Folder layout (see `project-structure`).
- Reporting (see `execution-reporting`).
