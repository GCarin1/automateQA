"""Run settings: one TOML file per environment, overridden by env vars."""

from __future__ import annotations

import os
import tomllib
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
DEFAULT_ENV = "local"
DEFAULT_TIMEOUT_MS = 5000

# Setting name -> environment variable that overrides it.
ENV_VARS = {
    "base_url": "BASE_URL",
    "serve_dir": "SERVE_DIR",
    "timeout_ms": "TIMEOUT_MS",
    "user_name": "TEST_USER_NAME",
    "user_password": "TEST_USER_PASSWORD",
}


class ConfigurationError(Exception):
    """Raised before any browser opens when the run settings are unusable."""


@dataclass(frozen=True)
class Settings:
    env: str
    base_url: str
    serve_dir: str
    timeout_ms: int
    user_name: str
    user_password: str

    def __repr__(self) -> str:
        # Never leak the password into logs or reports.
        return (
            f"Settings(env={self.env!r}, base_url={self.base_url!r}, "
            f"serve_dir={self.serve_dir!r}, timeout_ms={self.timeout_ms}, "
            f"user_name={self.user_name!r}, user_password='***')"
        )


def load_settings(
    environ: Mapping[str, str] | None = None,
    config_dir: Path = CONFIG_DIR,
) -> Settings:
    """Build the settings for the environment named by ``TEST_ENV``."""
    environ = os.environ if environ is None else environ
    env = environ.get("TEST_ENV") or DEFAULT_ENV
    config_file = config_dir / f"{env}.toml"
    if not config_file.is_file():
        raise ConfigurationError(f"TEST_ENV={env!r}: config file {config_file} not found")

    values = tomllib.loads(config_file.read_text(encoding="utf-8"))
    for key, var in ENV_VARS.items():
        if environ.get(var):
            values[key] = environ[var]

    missing = [ENV_VARS[k] for k in ("user_name", "user_password") if not values.get(k)]
    if not values.get("base_url") and not values.get("serve_dir"):
        missing.append(f"{ENV_VARS['base_url']} (or {ENV_VARS['serve_dir']})")
    if missing:
        raise ConfigurationError(f"missing required settings: {', '.join(missing)}")

    try:
        timeout_ms = int(values.get("timeout_ms", DEFAULT_TIMEOUT_MS))
    except ValueError as error:
        raise ConfigurationError(f"{ENV_VARS['timeout_ms']} must be an integer") from error

    return Settings(
        env=env,
        base_url=str(values.get("base_url", "")),
        serve_dir=str(values.get("serve_dir", "")),
        timeout_ms=timeout_ms,
        user_name=str(values["user_name"]),
        user_password=str(values["user_password"]),
    )
