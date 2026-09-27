# Spec — ci-pipeline

**Capability:** ci-pipeline
**Status:** draft
**Implementation:** planned
**Realizes:** SC5, SC4
**Depends on:** execution-reporting, configuration
**Last updated:** 2026-09-27
**Version:** 0.1.0

## Purpose

Ship a working CI workflow that installs the template, runs the architecture checks and the example suite on every push and pull request, and publishes the reports, so adopters inherit a green pipeline instead of a broken one.

## Requirements (EARS)

### Ubiquitous

- The template shall include a GitHub Actions workflow that runs on every push and pull request.
- The workflow shall run lint, architecture checks and the example suite, in that order.
- The workflow shall use currently supported action major versions and a supported Python version.

### Event-driven

- When any step fails, the workflow shall fail the job.
- When the job finishes, the workflow shall upload the `artifacts/` folder, pass or fail.

### Unwanted-behavior (must-not)

- The workflow shall not require any repository secret to run the example suite.

### Optional

- Where an adopter uses another CI system, the template may document the equivalent commands in the README.

## Acceptance criteria

1. [unverified] The workflow run on the default branch is green — verified by `.github/workflows/tests.yml`.
2. [unverified] A failing test makes the workflow job fail and still uploads artifacts/ — verified by `.github/workflows/tests.yml`.

## Maturity

**MVP (committed):**

- One GitHub Actions workflow: lint, architecture checks, example suite, artifact upload.

**Future (aspirational, not committed):**

- GitLab CI and Azure Pipelines examples.
- Scheduled nightly regression run.

## Out of scope for this spec

- Deployment of any application.
