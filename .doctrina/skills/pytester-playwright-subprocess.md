---
name: pytester-playwright-subprocess
description: Run a Playwright UI test inside pytester without losing the installed browsers.
when: A framework self-check uses pytester (runpytest_subprocess or runpytest) to run a test that opens a browser.
---

# Skill — pytester-playwright-subprocess

## When to use this skill

- Adding or changing a test in `tests/framework/` that runs an inner pytest
  session with pytester, where the inner test uses the `page` fixture or any
  business fixture that opens a browser (e.g. `tests/framework/test_evidence.py`).

## Procedure

1. Capture the real home at import time, before the `pytester` fixture runs:
   `REAL_HOME = os.environ.get("HOME", "")`.
2. In the fixture that prepares the run, restore it with
   `monkeypatch.setenv("HOME", REAL_HOME)`, and set `PYTHONPATH` to the
   project root so `-p core.plugin -p business.fixtures` import.
3. Reproduce the CI condition locally before pushing:
   `env -u PLAYWRIGHT_BROWSERS_PATH HOME=<dir with .cache/ms-playwright> pytest tests/framework/test_evidence.py`.

## Anti-patterns

- Trusting a local green run where `PLAYWRIGHT_BROWSERS_PATH` is exported:
  pytester points `HOME` at a temporary folder, Playwright then looks for
  browsers under the fake home, and the inner session errors with
  "Executable doesn't exist ... playwright install" only in CI (seen in
  GitHub Actions run 36293277897).

## Related material

- `.doctrina/specs/execution-reporting/spec.md` (evidence criterion)
- ADR 0002 — pytest + Playwright
