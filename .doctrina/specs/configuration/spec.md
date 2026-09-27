# Spec — configuration

**Capability:** configuration
**Status:** draft
**Implementation:** planned
**Realizes:** SC3, SC4
**Depends on:** project-structure
**Last updated:** 2026-09-27
**Version:** 0.1.0

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

- The template shall not version any `.env` file, credential or real company URL.
- The template shall not print secret values in logs or reports.

### Optional

- Where a remote grid is used, the template may read its endpoint and credentials from environment variables through the same loader.

## Acceptance criteria

1. [unverified] Running the suite with TEST_ENV unset targets the local example SUT — verified by `tests/unit/test_settings.py`.
2. [unverified] An environment variable overrides the value from the environment file — verified by `tests/unit/test_settings.py`.
3. [unverified] A missing required setting raises a configuration error naming the variable — verified by `tests/unit/test_settings.py`.
4. [unverified] .gitignore excludes .env and a secret-scan step in CI finds no secrets — verified by `.github/workflows/tests.yml`.

## Maturity

**MVP (committed):**

- Environment files, env-var override, `.env.example`, fail-fast on missing settings.

**Future (aspirational, not committed):**

- Integration with a secret manager (Vault, AWS Secrets Manager).

## Out of scope for this spec

- Driver capabilities of paid grids.
