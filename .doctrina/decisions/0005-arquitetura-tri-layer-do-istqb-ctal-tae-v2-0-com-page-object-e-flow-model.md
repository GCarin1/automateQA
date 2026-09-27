# ADR 0005 — Arquitetura Tri-Layer do ISTQB CTAL-TAE v2.0 com Page Object e Flow Model

- **Status:** accepted
- **Date:** 2026-09-27
- **Deciders:** dono do repositório (GCarin1)
- **Supersedes:** —
- **Superseded by:** —
- **Evidence:** n/a — nenhuma implementação ainda; o change do walking skeleton será citado via `doctrina decision land`
- **Landed:** 2026-09-27 — `tests/framework/test_layers.py`, `README.md`

## Context

O dono pediu que a arquitetura siga o que há de mais atual no ISTQB. A
versão vigente é o syllabus CTAL-TAE v2.0 (2024-05-03). A ADR 0001
(rejeitada) propunha quatro camadas e flows inspirados no Screenplay; o
syllabus v2.0 recomenda outra forma:

- §3.1.1 — gTAA: capacidades de geração (opcional), definição, execução e
  adaptação de testes, com interfaces para SUT, gestão de projeto, gestão
  de testes e gestão de configuração (CI/CD, ambientes, testware).
- §3.1.3 — camadas do TAF, "manter o número de camadas baixo": Test
  scripts (repositório de casos de teste e anotações de suíte; chama só a
  camada de negócio, nunca as core libraries), Business logic (tudo que
  depende do SUT; herda ou usa fachadas das core libraries) e Core
  libraries (tudo que independe do SUT, reutilizável entre projetos da
  mesma stack). Referência: Földházi, "Tri-Layer Testing Architecture"
  (PNSQC).
- §3.1.5 — princípios de OO e SOLID; padrões facade, singleton (um único
  driver falando com o SUT), page object model e flow model (fachada
  dupla sobre os page objects, com as ações de usuário reutilizáveis).
- §4.3.1 — clean code (Robert C. Martin): nomes significativos, estrutura
  comum, sem hardcoding (dados vindos de fonte comum), métodos curtos e
  com poucos parâmetros, logging, analisadores estáticos e formatadores.

## Decision

O template adota as três camadas do TAF do CTAL-TAE v2.0, com dependência
apenas para baixo:

1. **Test scripts** — `tests/e2e/`: casos de teste e marcadores. Recebem
   flows e pages por fixtures e fazem as asserções. Não importam `core/`
   nem o driver (Playwright).
2. **Business logic** — `business/`: tudo que depende do SUT.
   `business/pages/` (page objects, herdam a fachada base de `core/`),
   `business/flows/` (flow model: ações de usuário compostas de page
   objects), `business/data/` (dados de teste) e `business/fixtures.py`
   (monta pages e flows para os testes).
3. **Core libraries** — `core/`: tudo que independe do SUT e pode ser
   copiado para outro projeto Python + Playwright: carregamento de
   configuração, fachada base de página, servidor estático, plugin pytest
   (driver singleton por sessão via pytest-playwright, timeouts,
   evidências).

O runner (pytest) cobre a capacidade de execução da gTAA; `config/` e o
CI cobrem a interface de gestão de configuração. A geração de testes fica
fora do escopo. Os testes do próprio template (arquitetura, configuração,
marcadores) ficam em `tests/framework/` e são autorizados a importar
`core/`.

## Alternatives considered

1. Quatro camadas com flows inspirados no Screenplay (ADR 0001, rejeitada) —
   mais camadas do que o syllabus recomenda e vocabulário que não está no
   CTAL-TAE v2.0.
2. Screenplay completo (actors, abilities, tasks, questions) — boa aderência
   a SOLID, mas não é padrão citado pelo syllabus e eleva a curva de
   adoção de um template.
3. Page Object puro, sem flow model — o syllabus trata o flow model como a
   evolução que permite reutilizar passos entre scripts; sem ele os testes
   repetem sequências de páginas.

## Consequences

**Positive**

- Estrutura justificável por citação direta de um padrão internacional
  vigente, útil em qualquer empresa.
- Trocar de sistema alvo afeta só `business/` e `config/`; `core/` é
  reaproveitável entre projetos (§3.1.3, figura 3).
- Regras de dependência verificáveis por teste de arquitetura.

**Negative**

- Os testes não usam o `expect` do Playwright diretamente; as pages
  expõem métodos de consulta que esperam e devolvem valores, e o teste usa
  `assert` simples.

**Neutral**

- Substitui a proposta da ADR 0001, que foi rejeitada antes de ser aceita.
