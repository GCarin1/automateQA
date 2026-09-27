import tomllib

from _source import ROOT

ADDOPTS = tomllib.loads((ROOT / "pyproject.toml").read_text())["tool"]["pytest"]["ini_options"][
    "addopts"
]


def test_every_run_writes_junit_and_html_reports(pytester):
    report_opts = [
        opt.replace("artifacts/", f"{pytester.path}/artifacts/")
        for opt in ADDOPTS
        if opt.startswith(("--junitxml", "--html", "--self-contained-html"))
    ]
    pytester.makepyfile("def test_passing_example_writes_reports():\n    pass\n")

    result = pytester.runpytest_subprocess(*report_opts, "-p", "no:randomly")

    result.assert_outcomes(passed=1)
    assert (pytester.path / "artifacts" / "junit.xml").is_file()
    assert (pytester.path / "artifacts" / "report.html").is_file()


def test_run_with_zero_collected_tests_fails(pytester):
    result = pytester.runpytest_subprocess("-p", "no:randomly")

    assert result.ret != 0
