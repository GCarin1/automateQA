from __future__ import annotations

from core.base_page import BasePage


class HomePage(BasePage):
    path = "/home.html"

    @property
    def _welcome(self):
        return self.page.get_by_test_id("welcome-message")

    @property
    def _logout_button(self):
        return self.page.get_by_test_id("logout-button")

    def welcome_message(self) -> str:
        return self.text_of(self._welcome)

    def sign_out(self) -> None:
        self.click(self._logout_button)
