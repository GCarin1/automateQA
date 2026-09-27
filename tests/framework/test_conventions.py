"""Clean-code rules of the test-authoring spec, enforced on the sources."""

import ast

import pytest
from _source import parse, python_files, relative

TEMPLATE_CODE = list(python_files("core", "business", "tests"))


def _is_sleep(node):
    if isinstance(node, ast.Attribute):
        return node.attr == "sleep"
    if isinstance(node, ast.ImportFrom):
        return node.module == "time" and any(a.name == "sleep" for a in node.names)
    return False


def _sleep_calls(tree):
    return [node.lineno for node in ast.walk(tree) if _is_sleep(node)]


def _swallowed_exceptions(tree):
    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue
        bare = node.type is None
        only_pass = all(isinstance(stmt, ast.Pass) for stmt in node.body)
        if bare or only_pass:
            yield node.lineno


@pytest.mark.parametrize("path", TEMPLATE_CODE, ids=relative)
def test_no_fixed_sleeps(path):
    lines = list(_sleep_calls(parse(path)))

    assert lines == [], f"{relative(path)} sleeps on lines {lines}; wait on a condition"


@pytest.mark.parametrize("path", TEMPLATE_CODE, ids=relative)
def test_no_swallowed_exceptions(path):
    lines = list(_swallowed_exceptions(parse(path)))

    assert lines == [], f"{relative(path)} swallows exceptions on lines {lines}"


@pytest.mark.parametrize("path", list(python_files("tests/e2e")), ids=relative)
def test_test_names_describe_behaviour_and_result(path):
    names = [
        n.name
        for n in ast.walk(parse(path))
        if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
    ]
    too_short = [name for name in names if len(name.split("_")) < 4]

    assert names, f"{relative(path)} has no tests"
    assert too_short == [], f"use test_<behaviour>_<expected_result>: {too_short}"
