
# AutomateQA

AutomateQA é um template robusto e flexível para automação de testes web, desenvolvido em Python, utilizando as bibliotecas Selenium, Behave e o BrowserStack-SDK. Este projeto fornece uma estrutura organizada e pronta para uso, permitindo que você crie e execute testes automatizados de forma eficiente em diferentes navegadores e dispositivos.

## Características Principais

* **Behave Integration** : Utilize o Behave para escrever testes BDD (Behavior-Driven Development) de maneira fácil e compreensível.
* **Selenium WebDriver** : Integre facilmente o Selenium WebDriver para interagir com os elementos da web e simular ações do usuário.
* **Cross-browser Testing com BrowserStack** : Teste sua aplicação em vários navegadores e dispositivos usando o BrowserStack, garantindo a compatibilidade em diferentes ambientes.
* **Estrutura Organizada** : Siga uma estrutura clara e modular para organizar seus testes e scripts de automação.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o Python em seu ambiente. Além disso, é necessário instalar as dependências do projeto, o que pode ser feito executando o seguinte comando:

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
</code></div></div></pre>

## Configuração do BrowserStack

1. Crie uma conta no [BrowserStack](https://www.browserstack.com/).
2. Obtenha suas credenciais de acesso.
3. Substitua as informações no arquivo `config.yaml` com suas credenciais.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>yaml</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-yaml">browserstack:
  username: SEU_USERNAME
  access_key: SUA_CHAVE_DE_ACESSO
</code></div></div></pre>

## Estrutura do Projeto

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>plaintext</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-plaintext">automateQA/
|-- drivers/
|-- features/
|   |-- steps/
|       |-- example_steps.py
|       |-- environment.py
|-- pages/
|   |-- mapeamento.py
|   |-- test_example.py
|-- .gitignore
|-- config.yaml
|-- browserstack.yaml
|-- requirements.txt
|-- README.md
</code></div></div></pre>

* **features/steps** : Contém os arquivos de passos para os cenários do Behave.
* **drivers** : Armazena o arquivo `chromedriver.py`
* **pages** : Pasta opcional para testes adicionais usando o Selenium diretamente, sem Behave.
* **.gitignore** : Arquivo para especificar quais arquivos e pastas devem ser ignorados pelo Git.
* **config.yaml** : Arquivo de configuração para variaveis.
* **browserstack.yaml** : Arquivo de configuração para suas credenciais do BrowserStack.
* **requirements.txt** : Lista de dependências do projeto.

## Executando os Testes

Para executar os testes, utilize o seguinte comando no terminal:

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">behave
browserstack-sdk
</code></div></div></pre>

Isso executará todos os cenários de teste definidos na pasta `features`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar este template.
