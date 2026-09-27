# automateQA — Product

## Vision

automateQA é um template de referência para automação de testes em Python:
um padrão de organização de pastas, de camadas e de escrita de testes que
qualquer time ou empresa consegue clonar, entender em minutos e adaptar ao
próprio sistema trocando apenas a camada de adaptação e a configuração. O
valor está no padrão, não em testar um sistema específico.

## Problem

Cada time recria do zero a estrutura da sua automação, e o resultado
costuma repetir os mesmos defeitos que o próprio repositório legado
exibe hoje: locators acoplados a um único sistema, esperas que engolem
exceções e deixam o teste passar em falso, credenciais misturadas à
configuração, caminhos de import que só funcionam num diretório, CI que
não executa e nenhuma separação entre intenção do teste e detalhe de UI.
Não existe um ponto de partida curto, agnóstico de empresa e alinhado a
uma arquitetura reconhecida (gTAA do ISTQB CTAL-TAE v2.0).

## Target users

- Analistas de QA e SDETs que iniciam uma suíte de automação web em Python
  e querem um esqueleto pronto e opinativo.
- Líderes de QA que precisam de um padrão comum para todos os times
  e projetos de automação de uma empresa.
- Desenvolvedores que precisam escrever testes E2E seguindo o mesmo
  padrão do time de QA.

## Scope

In scope:

- Estrutura de pastas em camadas, mapeada às camadas da gTAA (definição,
  execução, adaptação) e documentada.
- Convenções de escrita de testes: nomes, padrão Arrange-Act-Assert,
  Page/Component Objects, estratégia de locators, esperas explícitas.
- Configuração por ambiente com segredos fora do repositório.
- Execução local com um comando, seleção por marcadores, evidências
  (screenshot/trace) em falha e relatório legível por CI.
- Um SUT de demonstração em HTML estático dentro do repositório, com uma
  suíte de exemplo que roda sem rede externa.
- Pipeline de CI de exemplo que executa a suíte de exemplo.

Out of scope (deferred or rejected):

- Testes de API, mobile, performance e segurança (candidatos a módulos
  futuros; a estrutura não deve impedi-los).
- Integração com grids pagos (BrowserStack, Sauce Labs) como parte do
  núcleo — no máximo documentada como ponto de extensão.
- Ferramenta de gestão de testes, dashboards e geração de testes por IA.

## Non-goals

- Não é uma biblioteca publicada no PyPI nem um framework com API própria.
- Não é uma suíte de testes de um produto real.
- Não tenta suportar todos os runners e drivers ao mesmo tempo: escolhe um
  padrão e documenta como trocar.

## Success criteria

- [SC1] Um usuário novo clona o repositório, instala as dependências e
  executa a suíte de exemplo com sucesso usando no máximo 3 comandos
  documentados no README.
- [SC2] Cada pasta do template tem uma única responsabilidade documentada,
  mapeada a uma camada da gTAA, e nenhum teste importa o driver de
  automação diretamente.
- [SC3] Adaptar o template a um sistema real exige alterar apenas a
  configuração e a camada de adaptação (pages/components/flows), sem
  tocar no núcleo.
- [SC4] Nenhum segredo, URL de ambiente real ou dado de empresa fica
  versionado no repositório.
- [SC5] O CI executa a suíte de exemplo a cada push e pull request e falha
  quando um teste falha.
- [SC6] Toda falha de teste produz evidência (screenshot ou trace) e um
  relatório legível por máquina.

## Delivery order (walking skeleton)

1. SUT HTML de exemplo → um teste de login atravessando todas as camadas
   (teste → flow → page → núcleo) → execução local com um comando →
   evidência em falha → CI verde. Verificar com `doctrina verify` antes de
   expandir convenções, marcadores e documentação.
2. Configuração por ambiente e segredos.
3. Relatórios e marcadores.
4. Documentação do padrão (guia de adoção e de escrita de testes).
