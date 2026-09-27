import re

import pytest
from _source import ROOT

README = (ROOT / "README.md").read_text(encoding="utf-8")
GUIDE = (ROOT / "docs" / "writing-tests.md").read_text(encoding="utf-8")
LAYER_FOLDERS = {
    "tests/e2e/": "Test scripts",
    "business/": "Business logic",
    "core/": "Core libraries",
}
DOCUMENTED_FOLDERS = [*LAYER_FOLDERS, "config/", "demo_app/", "tests/framework/", "docs/"]


@pytest.mark.parametrize("folder", DOCUMENTED_FOLDERS)
def test_readme_folder_table_lists_every_folder(folder):
    assert re.search(rf"^\| `{re.escape(folder)}` \|", README, re.MULTILINE)


@pytest.mark.parametrize(("folder", "layer"), LAYER_FOLDERS.items())
def test_readme_maps_each_layer_folder_to_its_istqb_layer(folder, layer):
    assert re.search(rf"^\| `{re.escape(folder)}` \| {layer} \|", README, re.MULTILINE)


def _guide_sections():
    return re.split(r"^## (?=R\d+ )", GUIDE, flags=re.MULTILINE)[1:]


def test_writing_guide_covers_every_rule():
    rule_ids = [section.split()[0] for section in _guide_sections()]

    assert rule_ids == [f"R{n}" for n in range(1, 11)]


@pytest.mark.parametrize("section", _guide_sections(), ids=lambda s: s.split()[0])
def test_writing_guide_rule_has_correct_and_incorrect_example(section):
    assert "Correto" in section
    assert "Incorreto" in section
