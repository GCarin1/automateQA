# Spec Delta — capability: example-sut

**Operation:** MODIFIED
**Target spec on apply:** `.doctrina/specs/example-sut/spec.md`

---

```ops
set-header Status: active
set-header Implementation: verified — demo SUT and login suite (`tests/e2e/test_login.py`)
bump-version minor
replace-criterion 1: [verified] The example suite passes against the locally served demo SUT with no network access beyond dependency installation — verified by `tests/e2e/test_login.py`.
replace-criterion 2: [verified] The demo SUT is served for the session and the server is shut down after use — verified by `tests/framework/test_static_server.py`.
```
