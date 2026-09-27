import subprocess

import pytest
from _source import ROOT


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


@pytest.mark.parametrize("path", [".env", "artifacts/report.html"])
def test_secrets_and_run_output_are_git_ignored(path):
    assert _git("check-ignore", "-q", path).returncode == 0


def test_no_env_file_is_tracked():
    tracked = _git("ls-files").stdout.splitlines()

    assert [p for p in tracked if p.split("/")[-1] == ".env"] == []
