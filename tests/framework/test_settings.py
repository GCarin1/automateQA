import pytest

from core.settings import ConfigurationError, load_settings


@pytest.fixture
def config_dir(tmp_path):
    (tmp_path / "local.toml").write_text(
        'serve_dir = "demo_app"\nuser_name = "demo"\nuser_password = "secret"\n'
    )
    (tmp_path / "staging.toml").write_text('base_url = "https://staging.test"\n')
    return tmp_path


def test_unset_test_env_targets_local_demo_sut(config_dir):
    settings = load_settings(environ={}, config_dir=config_dir)

    assert (settings.env, settings.serve_dir, settings.base_url) == ("local", "demo_app", "")


def test_environment_variable_overrides_environment_file(config_dir):
    settings = load_settings(environ={"TIMEOUT_MS": "1234"}, config_dir=config_dir)

    assert settings.timeout_ms == 1234


def test_missing_required_setting_names_the_variable(config_dir):
    with pytest.raises(ConfigurationError, match="TEST_USER_NAME.*TEST_USER_PASSWORD"):
        load_settings(environ={"TEST_ENV": "staging"}, config_dir=config_dir)


def test_unknown_environment_is_rejected(config_dir):
    with pytest.raises(ConfigurationError, match="qa.toml not found"):
        load_settings(environ={"TEST_ENV": "qa"}, config_dir=config_dir)


def test_repr_hides_the_password(config_dir):
    settings = load_settings(environ={}, config_dir=config_dir)

    assert "secret" not in repr(settings)


def test_versioned_local_config_loads():
    settings = load_settings(environ={})

    assert settings.serve_dir == "demo_app"
