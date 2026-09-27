import tomllib

from _source import ROOT

PYTEST_OPTIONS = tomllib.loads((ROOT / "pyproject.toml").read_text())["tool"]["pytest"][
    "ini_options"
]


def test_markers_registry_is_strict():
    assert "--strict-markers" in PYTEST_OPTIONS["addopts"]


def test_unknown_marker_fails_collection(pytester):
    pytester.makeini(
        "[pytest]\naddopts = --strict-markers\nmarkers =\n"
        + "".join(f"    {marker}\n" for marker in PYTEST_OPTIONS["markers"])
    )
    pytester.makepyfile(
        "import pytest\n\n@pytest.mark.smokee\ndef test_typo_in_marker():\n    pass\n"
    )

    result = pytester.runpytest("-p", "no:randomly")

    assert result.ret != 0
    result.stdout.fnmatch_lines(["*'smokee' not found in `markers`*"])
