# ADR 0004 — Código em inglês, documentação em português

- **Status:** accepted
- **Date:** 2026-09-27
- **Deciders:** dono do repositório (GCarin1) — pendente de discussão
- **Supersedes:** —
- **Superseded by:** —
- **Evidence:** n/a — decisão ainda proposta
- **Landed:** 2026-09-27 — `core/settings.py`, `README.md`

## Context

O legado mistura português e inglês em nomes (`find_and_click`,
`substituir_mapeamento`, `Geral.acessou`). O template precisa ser adotável
por qualquer empresa, inclusive multinacionais.

## Decision

Proposto: identificadores, nomes de arquivos, marcadores e mensagens de
erro em inglês; README e guias em português (pt-BR), com possibilidade de
tradução futura.

## Alternatives considered

1. Tudo em português — mais acessível ao público inicial, porém mistura com APIs em inglês (pytest, Playwright) e dificulta adoção fora do Brasil.
2. Tudo em inglês — máxima portabilidade, mas perde o público-alvo brasileiro do dono.

## Consequences

**Positive**

- Código consistente com as bibliotecas usadas; documentação acessível ao público inicial.

**Negative**

- Duas línguas no repositório.

**Neutral**

- Specs do Doctrina seguem em inglês (EARS), product.md em português.
