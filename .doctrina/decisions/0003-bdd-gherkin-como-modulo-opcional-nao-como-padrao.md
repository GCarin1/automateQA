# ADR 0003 — BDD/Gherkin como módulo opcional, não como padrão

- **Status:** proposed
- **Date:** 2026-09-27
- **Deciders:** dono do repositório (GCarin1) — pendente de discussão
- **Supersedes:** —
- **Superseded by:** —
- **Evidence:** n/a — decisão ainda proposta
- **Landed:** —

## Context

O legado é 100% Behave, mas o `.feature` existente descreve cliques
("Aceitar cookies e recusar pesquisa e tour") em vez de comportamento, que é
o antipadrão mais comum de BDD. O template precisa servir tanto a times que
praticam BDD com o negócio quanto a times que não praticam.

## Decision

Proposto: o caminho padrão é teste pytest em Python (AAA) chamando
`flows/`. Gherkin fica como módulo opcional via pytest-bdd, cujos steps
chamam os mesmos `flows/` e nunca locators.

## Alternatives considered

1. BDD obrigatório (Behave ou pytest-bdd) — duplica cada teste em `.feature` + steps e só compensa quando o negócio lê/escreve os cenários.
2. Sem suporte a BDD — exclui empresas que exigem Gherkin.

## Consequences

**Positive**

- Menos camadas no caminho padrão; BDD continua possível sem refazer a arquitetura.

**Negative**

- Times acostumados ao Behave precisam migrar para pytest-bdd.

**Neutral**

- O módulo BDD fica como item Future em `test-authoring`.
