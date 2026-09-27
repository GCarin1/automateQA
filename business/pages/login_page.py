from __future__ import annotations

from core.base_page import BasePage


class LoginPage(BasePage):
    path = "/index.html"

    @property
    def _username(self):
        return self.page.get_by_label("Username")

    @property
    def _password(self):
        return self.page.get_by_label("Password")

    @property
    def _sign_in_button(self):
        return self.page.get_by_role("button", name="Sign in")

    @property
    def _error(self):
        return self.page.get_by_test_id("login-error")

    @property
    def _heading(self):
        return self.page.get_by_role("heading", level=1)

    def sign_in(self, name: str, password: str) -> None:
        self.fill(self._username, name)
        self.fill(self._password, password, secret=True)
        self.click(self._sign_in_button)

    def error_message(self) -> str:
        return self.text_of(self._error)

    def heading(self) -> str:
        return self.text_of(self._heading)
