"""pytest plugin with the SUT-independent fixtures of the framework.

Registered by the root ``conftest.py``. It builds on pytest-playwright, which
keeps one browser per session (the singleton driver of CTAL-TAE v2.0 §3.1.5)
and a fresh context and page per test.
"""

from __future__ import annotations

from collections.abc import Iterator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import BrowserContext, Page

from core.settings import PROJECT_ROOT, Settings, load_settings
from core.static_server import serve_directory


def pytest_configure(config: pytest.Config) -> None:
    # A local .env fills gaps; variables already exported always win.
    load_dotenv(PROJECT_ROOT / ".env", override=False)


@pytest.fixture(scope="session")
def settings() -> Settings:
    return load_settings()


@pytest.fixture(scope="session")
def base_url(request: pytest.FixtureRequest, settings: Settings) -> Iterator[str]:
    """Override pytest-base-url: CLI --base-url > BASE_URL > served folder."""
    cli_url = request.config.getoption("base_url", default=None)
    if cli_url or settings.base_url:
        yield cli_url or settings.base_url
        return
    with serve_directory(PROJECT_ROOT / settings.serve_dir) as url:
        yield url


@pytest.fixture
def page(context: BrowserContext, settings: Settings) -> Page:
    """Override pytest-playwright's page to apply the configured timeout."""
    new_page = context.new_page()
    new_page.set_default_timeout(settings.timeout_ms)
    return new_page
