"""Login feature of the demo SUT: test scripts layer (CTAL-TAE v2.0 §3.1.3)."""

import pytest


@pytest.mark.smoke
def test_login_with_valid_credentials_shows_welcome_message(auth_flow, valid_user):
    # Arrange: valid_user comes from settings.
    # Act
    home_page = auth_flow.login_as(valid_user)
    # Assert
    assert home_page.welcome_message() == f"Welcome, {valid_user.name}!"


@pytest.mark.regression
def test_login_with_wrong_password_shows_error(auth_flow, invalid_user):
    login_page = auth_flow.attempt_login(invalid_user)

    assert login_page.error_message() == "Invalid username or password."


@pytest.mark.regression
def test_logout_returns_to_sign_in_page(auth_flow, valid_user):
    auth_flow.login_as(valid_user)

    login_page = auth_flow.logout()

    assert login_page.heading() == "Sign in"
