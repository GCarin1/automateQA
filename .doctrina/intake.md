# Intake — automateQA

- **Status:** converted
- **Date:** 2026-09-27
- **Source:** ../../../tmp/claude-0/-home-user-automateQA/b846e8f1-a1f0-5027-bda6-9d05de243b46/scratchpad/intake.txt

<!-- Raw project intent, stored verbatim. The bootstrap playbook
     (doctrina intake) converts it into product.md and capability
     specs. Close it with `doctrina intake --converted`; after that the
     specs are the only source of truth; never edit this file to
     change requirements. -->

---

automateQA — template de automação de testes; padronização da criação de testes automatizados.

Intenção do dono (sessão de 2026-09-27, palavras do dono resumidas):
- O projeto é um TEMPLATE: um padrão a ser seguido, não um produto com um intuito de negócio próprio.
- Pode conter um exemplo executável com um HTML local dentro do repositório (SUT de demonstração), mas o foco agora é apenas padronização.
- A padronização precisa se encaixar em qualquer lugar ou empresa: fácil acesso, padrão acessível e rápido de adotar (clonar, instalar, rodar, trocar o exemplo pelo sistema real).
- O repositório é antigo (Behave + Selenium + BrowserStack, locators acoplados a um sistema específico, credenciais em config.yml, CI quebrado) e a ideia é atualizá-lo; pode-se mudar tudo se necessário.
- A organização de pastas e o modo de criação da automação devem seguir um padrão reconhecido (pesquisa: arquitetura genérica de automação gTAA do ISTQB CTAL-TAE v2.0, Page Object/Component Object, Screenplay, princípios SOLID/clean code, pirâmide de testes).
- O dono programa principalmente em Python e é analista de qualidade de software.
