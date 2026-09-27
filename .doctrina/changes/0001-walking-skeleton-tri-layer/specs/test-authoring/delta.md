# Spec Delta — capability: test-authoring

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/test-authoring/spec.md`

---

```ops
set-header Status: active
set-header Implementation: verified — rules R1–R10 (`docs/writing-tests.md`)
bump-version minor
replace-requirement ubiquitous 3: Page objects shall expose intention-revealing methods (for example `sign_in(name, password)`) and return page objects or values, never raw driver elements.
replace-requirement unwanted 1: The template shall not use fixed sleeps (`time.sleep`) in `core/`, `business/` or `tests/`.
replace-requirement optional 1: Where a team adopts BDD, the template may bind Gherkin feature files to the same flows through pytest-bdd, keeping step definitions free of locators.
append-requirement ubiquitous: Assertions shall be made only in test scripts, on values returned by pages and flows.
replace-criterion 1: [verified] A static check fails the build when a fixed sleep appears under core/, business/ or tests/ — verified by `tests/framework/test_conventions.py`.
replace-criterion 2: [verified] A static check fails the build when a bare except or an except block containing only pass appears in the template code — verified by `tests/framework/test_conventions.py`.
replace-criterion 3: [verified] The example suite runs green in random order — verified by `tests/e2e/test_login.py`.
replace-criterion 4: [verified] The guide docs/writing-tests.md documents rules R1 to R10, each with a correct and an incorrect example — verified by `tests/framework/test_docs.py`.
append-criterion [verified] A wait timeout raises an error that names the locator and the timeout — verified by `tests/framework/test_base_page.py`.
append-criterion [verified] A static check fails the build when a test name does not follow test_<behaviour>_<expected_result> — verified by `tests/framework/test_conventions.py`.
```
