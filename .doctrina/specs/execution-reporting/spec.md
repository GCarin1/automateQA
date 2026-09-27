# Spec — execution-reporting

**Capability:** execution-reporting
**Status:** draft
**Implementation:** planned
**Realizes:** SC1, SC6
**Depends on:** configuration, project-structure
**Last updated:** 2026-09-27
**Version:** 0.1.0

## Purpose

Run the suite with one command, select subsets by marker, and turn every failure into evidence and a machine-readable report so failures are diagnosed without re-running.

## Requirements (EARS)

### Ubiquitous

- The template shall run the full suite with one documented command.
- The template shall let a run select tests by marker (for example `smoke`, `regression`) and declare every marker in one registry that rejects unknown markers.
- The template shall produce a JUnit XML report and a human-readable HTML report for every run.

### Event-driven

- When a test fails, the template shall save a screenshot and a browser trace named after the test into the run's artifacts folder.
- When a run finishes, the template shall exit with a non-zero code if any test failed or errored.

### State-driven

- While running headless, the template shall produce the same evidence as a headed run.

### Unwanted-behavior (must-not)

- The template shall not write artifacts into the source folders.
- The template shall not report a run as passed when zero tests were collected.

### Optional

- Where parallel execution is enabled, the template may run tests in parallel workers without shared state.

## Acceptance criteria

1. [unverified] A deliberately failing example test leaves a screenshot and a trace under artifacts/ — verified by `tests/e2e/test_evidence.py`.
2. [unverified] A run writes artifacts/junit.xml and artifacts/report.html — verified by `.github/workflows/tests.yml`.
3. [unverified] An unknown marker makes the run fail at collection — verified by `tests/unit/test_markers.py`.

## Maturity

**MVP (committed):**

- One-command run, markers registry, JUnit + HTML report, screenshot and trace on failure.

**Future (aspirational, not committed):**

- Allure report.
- Parallel execution as default.
- Video recording on failure.

## Out of scope for this spec

- CI wiring (see `ci-pipeline`).
