# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [Unreleased]

### Added

- Arquitetura Tri-Layer do ISTQB CTAL-TAE v2.0: `tests/e2e/` (test scripts),
  `business/` (pages, flows, dados, fixtures) e `core/` (configuração,
  fachada base de página, servidor estático, plugin pytest).
- SUT de demonstração em `demo_app/` e suíte de login (válido, inválido,
  logout).
- Configuração por ambiente (`config/<TEST_ENV>.toml` + variáveis de
  ambiente + `.env`), com `.env.example`.
- Relatórios JUnit e HTML, screenshot e trace em falha, em `artifacts/`.
- Checagens automáticas de camadas, convenções, configuração, marcadores,
  evidências e documentação em `tests/framework/`.
- Workflow `.github/workflows/tests.yml`: secret scan, lint, checagens,
  suíte e upload de artifacts.
- `docs/writing-tests.md` com as regras R1–R10.

### Changed

- Runner e driver: Behave + Selenium 3 substituídos por pytest + Playwright.
- README reescrito para o novo padrão.

### Removed

- Código legado: `features/`, `drivers/`, `behave-path.yml`, `config.yml`,
  `.github/workflows/main.yml` e o suporte embutido ao BrowserStack.
