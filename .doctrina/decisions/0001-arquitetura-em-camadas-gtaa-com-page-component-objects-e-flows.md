# ADR 0001 — Arquitetura em camadas gTAA com Page/Component Objects e flows

- **Status:** proposed
- **Date:** 2026-09-27
- **Deciders:** dono do repositório (GCarin1)
- **Supersedes:** —
- **Superseded by:** —
- **Evidence:** n/a — nenhuma implementação ainda; o esqueleto do change de walking skeleton será citado via `doctrina decision land`
- **Landed:** —

## Context

O intake pede um padrão reconhecido de organização e de criação de automação
que sirva a qualquer empresa. O código legado mistura step, page e locator
(`features/pages/page_geral.py` chama `Utils` de `features/steps/`), acopla
locators a um sistema real e engole exceções. Referências consultadas:
ISTQB CTAL-TAE v2.0 (gTAA: camadas de geração, definição, execução e
adaptação), Page Object Model (Fowler), Screenplay (Marcano/Palmer) e
princípios SOLID aplicados a testes.

## Decision

O template adota quatro camadas com dependência apenas para baixo:
`tests/` (definição) → `flows/` (tarefas de negócio) → `pages/` +
`components/` (adaptação: locators e interações) → `core/` (driver,
configuração, evidências). A execução (gTAA) fica com o runner. Os
`flows/` são a parte "tarefa" do Screenplay sem atores/abilities, para
manter a curva de aprendizado baixa. Asserções ficam só em `tests/`.

## Alternatives considered

1. Page Object puro (sem flows) — simples, mas testes longos repetem sequências de páginas e as pages crescem com lógica de negócio (viola SRP).
2. Screenplay completo (actors, abilities, tasks, questions) — melhor aderência a SOLID e escala, porém curva alta para um template que deve ser adotado em minutos; pode ser adotado depois sobre os mesmos `flows/`.
3. Manter a estrutura legada `features/steps` + `features/pages` — acoplada ao Behave e sem separação de responsabilidades.

## Consequences

**Positive**

- Mapeamento direto a um padrão de mercado citável (ISTQB), fácil de justificar em qualquer empresa.
- Troca de sistema alvo afeta apenas `pages/`, `components/` e `flows/`.
- Regras de dependência verificáveis por teste de arquitetura.

**Negative**

- Uma camada a mais (`flows/`) do que o POM clássico; testes triviais podem parecer verbosos.

**Neutral**

- A camada de geração de testes da gTAA fica fora do escopo.
