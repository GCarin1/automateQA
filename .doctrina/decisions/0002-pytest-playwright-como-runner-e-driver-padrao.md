# ADR 0002 — pytest + Playwright como runner e driver padrão

- **Status:** accepted
- **Date:** 2026-09-27
- **Deciders:** dono do repositório (GCarin1) — pendente de discussão
- **Supersedes:** —
- **Superseded by:** —
- **Evidence:** n/a — decisão ainda proposta
- **Landed:** —

## Context

O legado usa Behave + Selenium 3 (`webdriver.Chrome(ChromeDriverManager().install())`,
`desired_capabilities`, removidos no Selenium 4) + webdriver_manager 3.5 e
BrowserStack SDK, e não roda mais como está. É preciso escolher runner e
driver atuais para o template.

## Decision

Proposto: pytest como runner (fixtures, marcadores, plugins de relatório,
paralelismo via pytest-xdist) e Playwright para Python (`pytest-playwright`)
como driver: auto-wait, locators por papel acessível e `data-testid`, trace
viewer e screenshots nativos, browsers gerenciados pelo próprio pacote. O
driver fica isolado em `core/`, então trocar para Selenium afeta só essa
camada.

## Alternatives considered

1. pytest + Selenium 4 — padrão de mercado mais difundido e compatível com grids (BrowserStack/Selenium Grid); exige esperas explícitas manuais e não tem trace nativo.
2. Behave + Selenium (legado atualizado) — preserva o conhecimento atual, mas prende o template ao BDD e perde o ecossistema de fixtures/plugins do pytest.
3. Robot Framework — ótimo para times não programadores, porém outra linguagem de teste e fora do perfil Python do dono.

## Consequences

**Positive**

- Menos flakiness pelo auto-wait; evidências (trace, screenshot) quase sem código.
- Instalação em poucos comandos, sem gerenciar chromedriver.

**Negative**

- Empresas com grid Selenium ou contrato BrowserStack precisam de adaptação em `core/`.
- Parte do time pode conhecer apenas Selenium.

**Neutral**

- pytest também serve para futuros testes de API e unidade sem mudar de runner.
