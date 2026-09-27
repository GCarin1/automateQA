"""Test data for users: built from settings, never hardcoded in tests."""

from __future__ import annotations

from dataclasses import dataclass

from core.settings import Settings


@dataclass(frozen=True)
class User:
    name: str
    password: str

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, password='***')"


def registered_user(settings: Settings) -> User:
    return User(settings.user_name, settings.user_password)


def user_with_wrong_password(settings: Settings) -> User:
    return User(settings.user_name, f"{settings.user_password}-wrong")
