# Tasks — Change 0001-walking-skeleton-tri-layer

- [x] 1. Remover o legado: `features/`, `drivers/`, `behave-path.yml`, `config.yml`, `.github/workflows/main.yml`; atualizar `.gitignore`.
- [x] 2. `pyproject.toml` (pytest, ruff) e `requirements.txt` com as dependências atuais.
- [x] 3. `core/settings.py` + `config/local.toml` + `.env.example`, com testes em `tests/framework/test_settings.py`.
- [x] 4. `core/static_server.py`, `core/base_page.py` e `core/plugin.py` (base_url, timeout, driver por sessão).
- [x] 5. `demo_app/` — login, home e logout em HTML/JS estático com `data-testid` e labels acessíveis.
- [x] 6. `business/` — pages, flow de autenticação, dados de teste e fixtures.
- [x] 7. `tests/e2e/test_login.py` — login válido, inválido e logout, em ordem aleatória.
- [x] 8. `tests/framework/` — camadas, convenções, marcadores, evidências e documentação.
- [x] 9. `.github/workflows/tests.yml` — lint, checagens, suíte, secret scan, upload de artifacts.
- [x] 10. README, `docs/writing-tests.md`, `CHANGELOG.md` e Stack/Commands do AGENTS.md.
- [x] 11. Deltas das seis specs com critérios citando os testes reais; `doctrina verify` verde.
