"""Flow model (CTAL-TAE v2.0 §3.1.5): user actions over the page objects."""

from __future__ import annotations

from business.data.users import User
from business.pages.home_page import HomePage
from business.pages.login_page import LoginPage


class AuthFlow:
    def __init__(self, login_page: LoginPage, home_page: HomePage) -> None:
        self._login_page = login_page
        self._home_page = home_page

    def login_as(self, user: User) -> HomePage:
        self._login_page.open()
        self._login_page.sign_in(user.name, user.password)
        return self._home_page

    def attempt_login(self, user: User) -> LoginPage:
        self._login_page.open()
        self._login_page.sign_in(user.name, user.password)
        return self._login_page

    def logout(self) -> LoginPage:
        self._home_page.sign_out()
        return self._login_page
