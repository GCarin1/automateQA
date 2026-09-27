# Change 0001-walking-skeleton-tri-layer — walking skeleton tri-layer

- **Status:** applied
- **Applied:** 2026-09-27
- **Date:** 2026-09-27
- **Owner:** GCarin1 (agente: Claude Code)
- **Lane:** runtime (confident; signals: ci, configuracao) — opened anyway (--force)
- **Affects specs:** project-structure, test-authoring, configuration, execution-reporting, example-sut, ci-pipeline

<!--
Optional, and usually absent. The closing docs gate reads COMMAND and FLAG
names out of the prose below and asks for documentation when it finds any.
It cannot tell a change from a mention: explaining an effect, or writing a
Scope boundaries line about what this deliberately does NOT touch, names
things just as loudly as changing them would.

When that happens, say so on the record instead of forcing the close:

- **Documented surface:** n/a — names two commands to explain an effect; alters neither

`none` reads the same as `n/a`, and a BARE one silences nothing — the
reason is the declaration.
-->

## Why

Walking skeleton do template: alinhar as specs à arquitetura Tri-Layer do ISTQB CTAL-TAE v2.0 (ADR 0005), remover o código legado Behave/Selenium e entregar SUT HTML de demo, suíte de login atravessando tests → business → core com pytest + Playwright, configuração por ambiente, evidências e relatórios em falha, checagens de arquitetura e CI verde.

## What

Substitui todo o código legado (Behave + Selenium 3 + BrowserStack, locators
de um sistema real) pelo walking skeleton da arquitetura Tri-Layer (ADR 0005)
com pytest + Playwright (ADR 0002):

- `core/` — configuração por ambiente, fachada base de página, servidor
  estático, plugin pytest (base_url, timeout padrão, driver por sessão).
- `business/` — pages, flows (flow model), dados de teste e fixtures do SUT
  de demonstração.
- `tests/e2e/` — suíte de login; `tests/framework/` — checagens de
  arquitetura, convenções, configuração, marcadores e evidências.
- `demo_app/` — SUT HTML estático (login, home, logout).
- `config/`, `.env.example`, `pyproject.toml`, `requirements.txt`.
- `.github/workflows/tests.yml` substitui `main.yml`.
- README, `docs/writing-tests.md`, `CHANGELOG.md` e seção Stack/Commands do
  AGENTS.md.
- Deltas nas seis specs: caminhos e camadas passam a seguir o Tri-Layer do
  CTAL-TAE v2.0; critérios citam os testes reais.

## Scope boundaries

- Módulo BDD opcional (pytest-bdd) — continua em Future (ADR 0003).
- Grids remotos (BrowserStack/Selenium Grid) e execução paralela.
- Testes de API e mobile.

## Verification

<!--
How you will know the change is correctly applied. Use checkboxes: every
box here is a claim that must be PROVEN before the change is done.
`doctrina change archive` refuses to archive while any box below is
unchecked (pass --force to archive anyway and record the gap). Distinguish
"task marked done" from "verification passed" — link the evidence.
-->

- [x] Automated checks pass (`doctrina verify`, or the project's typecheck/test/build).
- [x] The affected spec's acceptance criteria are met and cite their evidence (`doctrina coverage`).

## Open questions

Nenhuma.
