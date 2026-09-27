# Spec — configuration

**Capability:** configuration
**Status:** active
**Implementation:** verified — settings loader (`tests/framework/test_settings.py`)
**Realizes:** SC3, SC4
**Depends on:** project-structure
**Last updated:** 2026-09-27
**Version:** 0.2.0

## Purpose

Load run settings (base URL, browser, headless, timeouts) per environment, and read secrets only from environment variables, so adopters swap the target system without editing code and never commit credentials.

## Requirements (EARS)

### Ubiquitous

- The template shall read settings from a versioned non-secret file per environment plus environment variables, with environment variables taking precedence.
- The template shall select the environment by one variable (`TEST_ENV`), defaulting to the local example environment.
- The template shall ship a `.env.example` listing every variable it reads, with placeholder values only.

### Event-driven

- When a required setting is missing, the template shall stop before opening a browser and report the missing variable name.

### Unwanted-behavior (must-not)

- The template shall not version any `.env` file, real credential or real company URL; the demo SUT's fake credentials in `config/local.toml` are test data, not secrets.
- The template shall not print secret values in logs or reports.

### Optional

- Where a remote grid is used, the template may read its endpoint and credentials from environment variables through the same loader.

## Acceptance criteria

1. [verified] Loading settings with TEST_ENV unset targets the local demo SUT — verified by `tests/framework/test_settings.py`.
2. [verified] An environment variable overrides the value from the environment file — verified by `tests/framework/test_settings.py`.
3. [verified] A missing required setting raises a configuration error naming the variable — verified by `tests/framework/test_settings.py`.
4. [verified] .gitignore excludes .env and run output, and no .env file is tracked — verified by `tests/framework/test_repository_hygiene.py`.
5. [verified] The settings representation hides the password — verified by `tests/framework/test_settings.py`.
6. [verified] The CI secret-scan step finds no secrets; observed in run 36293369635 — verified by `.github/workflows/tests.yml`.

## Maturity

**MVP (committed):**

- Environment files, env-var override, `.env.example`, fail-fast on missing settings.

**Future (aspirational, not committed):**

- Integration with a secret manager (Vault, AWS Secrets Manager).

## Out of scope for this spec

- Driver capabilities of paid grids.
