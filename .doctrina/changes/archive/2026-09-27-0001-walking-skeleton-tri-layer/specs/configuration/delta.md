# Spec Delta — capability: configuration

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/configuration/spec.md`

---

```ops
set-header Status: active
set-header Implementation: verified — settings loader (`tests/framework/test_settings.py`)
bump-version minor
replace-requirement unwanted 1: The template shall not version any `.env` file, real credential or real company URL; the demo SUT's fake credentials in `config/local.toml` are test data, not secrets.
replace-criterion 1: [verified] Loading settings with TEST_ENV unset targets the local demo SUT — verified by `tests/framework/test_settings.py`.
replace-criterion 2: [verified] An environment variable overrides the value from the environment file — verified by `tests/framework/test_settings.py`.
replace-criterion 3: [verified] A missing required setting raises a configuration error naming the variable — verified by `tests/framework/test_settings.py`.
replace-criterion 4: [verified] .gitignore excludes .env and run output, and no .env file is tracked — verified by `tests/framework/test_repository_hygiene.py`.
append-criterion [verified] The settings representation hides the password — verified by `tests/framework/test_settings.py`.
append-criterion [verified] The CI secret-scan step finds no secrets; observed in run 36293369635 — verified by `.github/workflows/tests.yml`.
```
