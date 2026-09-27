"""A failing UI test must leave a screenshot and a trace behind."""

import pytest
from _source import ROOT

FAILING_TEST = """
def test_deliberately_failing_login_leaves_evidence(auth_flow, valid_user):
    home_page = auth_flow.login_as(valid_user)
    assert home_page.welcome_message() == "this text is never shown"
"""


@pytest.fixture
def isolated_run(pytester, monkeypatch):
    monkeypatch.setenv("PYTHONPATH", str(ROOT))
    monkeypatch.setenv("TEST_ENV", "local")
    monkeypatch.setenv("SERVE_DIR", str(ROOT / "demo_app"))
    pytester.makepyfile(test_failing=FAILING_TEST)
    return pytester


def test_failure_saves_screenshot_and_trace(isolated_run):
    output = isolated_run.path / "evidence"

    result = isolated_run.runpytest_subprocess(
        "-p", "core.plugin",
        "-p", "business.fixtures",
        "-p", "no:randomly",
        f"--output={output}",
        "--screenshot=only-on-failure",
        "--tracing=retain-on-failure",
    )  # fmt: skip

    result.assert_outcomes(failed=1)
    assert list(output.rglob("*.png")), "no screenshot saved"
    assert list(output.rglob("trace.zip")), "no trace saved"
