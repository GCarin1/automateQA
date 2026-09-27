import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from core.base_page import BasePage


def test_wait_timeout_error_names_locator_and_timeout(page):
    base_page = BasePage(page)
    base_page.path = "/index.html"
    base_page.open()
    page.set_default_timeout(300)

    with pytest.raises(PlaywrightTimeoutError, match=r"(?s)300ms.*get_by_test_id\(\"missing\"\)"):
        base_page.text_of(page.get_by_test_id("missing"))
