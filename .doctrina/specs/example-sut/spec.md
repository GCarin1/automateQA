# Spec — example-sut

**Capability:** example-sut
**Status:** active
**Implementation:** verified — demo SUT and login suite (`tests/e2e/test_login.py`)
**Realizes:** SC1, SC3
**Depends on:** project-structure, test-authoring
**Last updated:** 2026-09-27
**Version:** 0.2.0

## Purpose

Provide a small static HTML system under test inside the repository, plus an example suite that exercises it through every layer, so the template demonstrates the standard end to end without network access or a real company system.

## Requirements (EARS)

### Ubiquitous

- The template shall include a static HTML SUT under `demo_app/` with a login page and a post-login page, using `data-testid` attributes and accessible labels.
- The template shall serve the SUT locally during the test session without external network access.
- The template shall include an example suite covering valid login, invalid login and logout through flows and pages.

### Event-driven

- When an adopter removes `demo_app/`, the template shall still run with a real `BASE_URL` after replacing the example pages and flows.

### Unwanted-behavior (must-not)

- The example SUT shall not reference any real company, brand or production URL.

## Acceptance criteria

1. [verified] The example suite passes against the locally served demo SUT with no network access beyond dependency installation — verified by `tests/e2e/test_login.py`.
2. [verified] The demo SUT is served for the session and the server is shut down after use — verified by `tests/framework/test_static_server.py`.

## Maturity

**MVP (committed):**

- Login, invalid login, logout pages and their example tests.

**Future (aspirational, not committed):**

- A form with validation and a table page to demonstrate components.

## Out of scope for this spec

- Backend logic; the SUT is static HTML and JavaScript only.
