# automateQA

Template de automação de testes web em Python que qualquer time ou empresa
pode clonar e adaptar. O valor dele está no **padrão**: estrutura de pastas,
camadas e regras de escrita de testes alinhadas à arquitetura **Tri-Layer do
ISTQB CTAL-TAE v2.0** (§3.1.3), com Page Object + Flow Model (§3.1.5) e
princípios de clean code (§4.3.1).

Stack: **pytest** (runner) + **Playwright** (driver), com relatórios JUnit e
HTML, screenshot e trace em caso de falha e um SUT HTML de demonstração que
roda sem rede.

## Início rápido

Requer Python 3.11 ou superior.

```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest
```

Por padrão a suíte roda contra o SUT de demonstração (`demo_app/`), servido
localmente numa porta livre. Os relatórios e as evidências vão para
`artifacts/`.

## Arquitetura

As dependências só apontam para baixo: test scripts → business logic → core
libraries. Os test scripts nunca chamam as core libraries (nem o Playwright)
diretamente.

| Pasta | Camada (CTAL-TAE v2.0) | Responsabilidade |
|---|---|---|
| `tests/e2e/` | Test scripts | Casos de teste e marcadores. Pedem flows, pages e dados por fixtures e fazem as asserções. |
| `business/` | Business logic | Tudo que depende do SUT: `pages/` (page objects e locators), `flows/` (flow model: ações de usuário), `data/` (dados de teste) e `fixtures.py`. |
| `core/` | Core libraries | Tudo que independe do SUT e pode ser reaproveitado em outro projeto: configuração, fachada base de página, servidor estático e plugin pytest. |
| `config/` | Gestão de configuração | Um arquivo TOML sem segredos por ambiente. |
| `demo_app/` | SUT de demonstração | HTML estático com login, home e logout. Remova ao adotar o template. |
| `tests/framework/` | Autoverificação do template | Checagens de camadas, convenções, configuração, marcadores e evidências. |
| `docs/` | Documentação | Guia de escrita de testes. |

```
automateQA/
├── conftest.py            # raiz de composição: registra core.plugin e business.fixtures
├── core/                  # core libraries (independentes do SUT)
├── business/
│   ├── pages/             # page objects: único lugar com locators
│   ├── flows/             # flow model: ações de usuário sobre as pages
│   ├── data/              # dados de teste
│   └── fixtures.py        # entrega pages, flows e dados aos testes
├── tests/
│   ├── e2e/               # test scripts
│   └── framework/         # checagens do próprio template
├── config/                # <ambiente>.toml
├── demo_app/              # SUT de demonstração
└── docs/writing-tests.md
```

## Configuração

O ambiente é escolhido por `TEST_ENV` (padrão: `local`), que carrega
`config/<TEST_ENV>.toml`. Variáveis de ambiente sobrepõem o arquivo, e um
`.env` local (nunca versionado) preenche o que não estiver exportado. Veja
`.env.example` para a lista completa.

| Variável | Uso |
|---|---|
| `TEST_ENV` | Nome do arquivo em `config/` |
| `BASE_URL` | URL do sistema sob teste |
| `SERVE_DIR` | Pasta servida localmente quando não há `BASE_URL` |
| `TIMEOUT_MS` | Timeout padrão das esperas |
| `TEST_USER_NAME`, `TEST_USER_PASSWORD` | Credenciais do usuário de teste (segredos) |

Se faltar uma configuração obrigatória, a execução para antes de abrir o
navegador e informa o nome da variável.

## Execução

```bash
pytest                      # tudo: checagens do template + suíte e2e
pytest tests/e2e            # só a suíte e2e
pytest -m smoke             # só testes marcados como smoke
pytest --headed             # com o navegador visível
pytest --browser firefox    # outro navegador (instale com playwright install)
pytest -p no:randomly       # desliga a ordem aleatória para depurar
```

Os marcadores ficam registrados em `pyproject.toml`, e um marcador
desconhecido falha a coleta. Os testes rodam em ordem aleatória
(pytest-randomly) para garantir que um não dependa do outro.

Saídas em `artifacts/`: `junit.xml`, `report.html` e, para cada teste que
falhou, screenshot e `trace.zip` em `artifacts/test-results/`. Para abrir o
trace: `playwright show-trace <arquivo>`.

## Adaptando a um sistema real

1. Crie `config/<ambiente>.toml` a partir de `config/example.toml` e exporte
   `TEST_ENV`, `BASE_URL`, `TEST_USER_NAME` e `TEST_USER_PASSWORD`.
2. Substitua `business/pages/`, `business/flows/`, `business/data/` e
   `business/fixtures.py` pelos do seu sistema.
3. Escreva os test scripts em `tests/e2e/` seguindo `docs/writing-tests.md`.
4. Remova `demo_app/` e o `serve_dir` de `config/local.toml`.

`core/` não precisa mudar. As checagens em `tests/framework/` garantem que as
regras de camadas continuam valendo.

## CI

`.github/workflows/tests.yml` roda a cada push e pull request: secret scan
(gitleaks), lint (ruff), checagens do template, suíte e2e e upload de
`artifacts/`. Não precisa de nenhum secret para rodar a suíte de exemplo.

## Referências

- ISTQB, *Certified Tester Advanced Level Test Automation Engineering
  (CTAL-TAE) v2.0*, 2024. §3.1.1 gTAA, §3.1.3 camadas do TAF, §3.1.5
  padrões, §4.3.1 manutenibilidade.
- P. Földházi, *Tri-Layer Testing Architecture*, PNSQC.
- Selenium Project, *Page object models*.
- R. C. Martin, *Clean Code*, 2008.

As decisões de arquitetura estão registradas em `.doctrina/decisions/`.
