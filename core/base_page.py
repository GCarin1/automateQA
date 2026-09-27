"""Facade over the Playwright page that every page object inherits."""

from __future__ import annotations

import logging

from playwright.sync_api import Locator, Page

logger = logging.getLogger(__name__)


class BasePage:
    """Hide driver details; expose intention-level helpers to page objects.

    Every helper waits explicitly for its element (bounded by the timeout
    configured on the page) and lets a timeout propagate: Playwright's error
    names the locator and the timeout, which is the evidence a failure needs.
    """

    path = "/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> BasePage:
        logger.info("open %s", self.path)
        self.page.goto(self.path)
        return self

    def click(self, locator: Locator) -> None:
        logger.info("click %s", locator)
        locator.click()

    def fill(self, locator: Locator, text: str, *, secret: bool = False) -> None:
        logger.info("fill %s with %s", locator, "***" if secret else repr(text))
        locator.fill(text)

    def text_of(self, locator: Locator) -> str:
        locator.wait_for(state="visible")
        return locator.inner_text().strip()
