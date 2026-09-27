import urllib.error
import urllib.request

import pytest

from core.static_server import serve_directory


def test_served_folder_is_reachable_and_shut_down_after_use(tmp_path):
    (tmp_path / "index.html").write_text("<h1>served</h1>")

    with serve_directory(tmp_path) as url:
        body = urllib.request.urlopen(f"{url}/index.html", timeout=5).read().decode()

    assert body == "<h1>served</h1>"
    with pytest.raises(urllib.error.URLError):
        urllib.request.urlopen(f"{url}/index.html", timeout=1)


def test_missing_folder_is_rejected(tmp_path):
    with pytest.raises(FileNotFoundError), serve_directory(tmp_path / "missing"):
        pass
