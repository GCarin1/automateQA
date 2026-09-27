"""Tri-Layer rules of ISTQB CTAL-TAE v2.0 §3.1.3, enforced on the sources."""

import ast

import pytest
from _source import imported_modules, parse, python_files, relative

DRIVER_PACKAGES = ("playwright", "selenium")


def _top_level(module: str) -> str:
    return module.split(".")[0]


@pytest.mark.parametrize("path", list(python_files("tests/e2e")), ids=relative)
def test_test_scripts_do_not_call_core_or_driver(path):
    forbidden = {"core", *DRIVER_PACKAGES}

    offenders = sorted(m for m in imported_modules(parse(path)) if _top_level(m) in forbidden)

    assert offenders == [], f"{relative(path)} imports {offenders}"


@pytest.mark.parametrize("path", list(python_files("business/flows")), ids=relative)
def test_flows_use_page_objects_not_the_driver(path):
    offenders = sorted(m for m in imported_modules(parse(path)) if _top_level(m) in DRIVER_PACKAGES)

    assert offenders == [], f"{relative(path)} imports {offenders}"


@pytest.mark.parametrize("path", list(python_files("core")), ids=relative)
def test_core_does_not_depend_on_business_or_tests(path):
    offenders = sorted(
        m for m in imported_modules(parse(path)) if _top_level(m) in {"business", "tests"}
    )

    assert offenders == [], f"{relative(path)} imports {offenders}"


@pytest.mark.parametrize("path", list(python_files("business", "core")), ids=relative)
def test_assertions_live_only_in_test_scripts(path):
    asserts = [n.lineno for n in ast.walk(parse(path)) if isinstance(n, ast.Assert)]

    assert asserts == [], f"{relative(path)} has assert on lines {asserts}"


def test_locators_live_only_in_page_objects():
    locator_calls = {"get_by_role", "get_by_label", "get_by_test_id", "get_by_text", "locator"}
    offenders = []
    for path in python_files("tests/e2e", "business/flows", "business/data"):
        for node in ast.walk(parse(path)):
            if isinstance(node, ast.Attribute) and node.attr in locator_calls:
                offenders.append(f"{relative(path)}:{node.lineno}")

    assert offenders == []
