# Design — Change 0001-walking-skeleton-tri-layer

## Approach

Três camadas conforme CTAL-TAE v2.0 §3.1.3 (ADR 0005). `conftest.py` na raiz
é a raiz de composição: registra `core.plugin` (fixtures independentes do
SUT) e `business.fixtures` (fixtures do SUT). Os testes em `tests/e2e/`
pedem apenas fixtures de negócio (`auth_flow`, `valid_user`) e fazem
`assert` sobre valores devolvidos pelas pages, sem importar `core` nem
`playwright`. O `core.plugin` sobrescreve `base_url` (do pytest-base-url,
usado pelo pytest-playwright) para servir `demo_app/` num servidor
estático local quando `serve_dir` está configurado, e sobrescreve `page`
para aplicar o timeout configurado. Evidências e relatórios vêm das
opções nativas do pytest-playwright e do pytest-html declaradas em
`addopts`, gravadas em `artifacts/`.

A configuração é lida de `config/<TEST_ENV>.toml` (stdlib `tomllib`),
sobreposta por variáveis de ambiente (e `.env` via python-dotenv, sem
sobrescrever variáveis já definidas).

## Alternatives considered

- Instalar o template como pacote (`pip install -e .`) — exige build
  backend e descoberta de pacotes; `pythonpath = ["."]` do pytest resolve
  os imports com um comando a menos.
- Usar o `expect` do Playwright nos testes — mais conciso, mas faria os
  test scripts chamarem uma core library, o que o §3.1.3 proíbe.
- pydantic-settings — validação rica, porém mais uma dependência para
  quatro valores; dataclass + tomllib basta.

## Trade-offs and risks

- Sobrescrever `base_url` e `page` depende da ordem de registro de
  plugins do pytest; coberto pela suíte e2e (se falhar, nenhum teste abre).
- As checagens de arquitetura são por AST, não um linter; cobrem os
  imports e padrões declarados, não todos os casos possíveis.

## Decisions to record as ADRs

Nenhuma nova — o change implementa as ADRs 0002, 0003, 0004 e 0005.
