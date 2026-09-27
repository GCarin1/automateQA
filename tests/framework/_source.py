"""Helpers to inspect the template's own Python sources with ast."""

from __future__ import annotations

import ast
from collections.abc import Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def python_files(*folders: str) -> Iterator[Path]:
    for folder in folders:
        yield from sorted((ROOT / folder).rglob("*.py"))


def parse(path: Path) -> ast.Module:
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def imported_modules(tree: ast.Module) -> Iterator[str]:
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            yield from (alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            yield node.module


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()
