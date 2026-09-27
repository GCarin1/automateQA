"""Fixtures that hand pages, flows and data to the test scripts."""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from business.data.users import User, registered_user, user_with_wrong_password
from business.flows.auth_flow import AuthFlow
from business.pages.home_page import HomePage
from business.pages.login_page import LoginPage
from core.settings import Settings


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def auth_flow(login_page: LoginPage, home_page: HomePage) -> AuthFlow:
    return AuthFlow(login_page, home_page)


@pytest.fixture
def valid_user(settings: Settings) -> User:
    return registered_user(settings)


@pytest.fixture
def invalid_user(settings: Settings) -> User:
    return user_with_wrong_password(settings)
