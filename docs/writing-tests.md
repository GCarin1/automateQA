# Guia de escrita de testes

Regras que todo teste do template segue. As regras marcadas com
*(verificada)* são checadas automaticamente em `tests/framework/`.

## R1 — Arrange, Act, Assert; um comportamento por teste

Separe preparação, ação e verificação. Cada teste verifica um único
comportamento.

Correto:

```python
def test_login_with_wrong_password_shows_error(auth_flow, invalid_user):
    login_page = auth_flow.attempt_login(invalid_user)

    assert login_page.error_message() == "Invalid username or password."
```

Incorreto:

```python
def test_login(auth_flow, valid_user, invalid_user):
    auth_flow.attempt_login(invalid_user)
    auth_flow.login_as(valid_user)
    auth_flow.logout()
    assert True
```

## R2 — Nome `test_<comportamento>_<resultado_esperado>` *(verificada)*

O módulo leva o nome da funcionalidade (`test_login.py`), e o teste diz o
que faz e o que espera.

Correto:

```python
def test_logout_returns_to_sign_in_page(auth_flow, valid_user): ...
```

Incorreto:

```python
def test_logout(auth_flow): ...
def test_caso_03(auth_flow): ...
```

## R3 — Test scripts não chamam core nem o driver *(verificada)*

Testes recebem flows, pages e dados por fixtures e nunca importam `core` ou
`playwright` (CTAL-TAE v2.0 §3.1.3).

Correto:

```python
def test_login_with_valid_credentials_shows_welcome_message(auth_flow, valid_user):
    home_page = auth_flow.login_as(valid_user)
    assert home_page.welcome_message() == f"Welcome, {valid_user.name}!"
```

Incorreto:

```python
from playwright.sync_api import expect


def test_login(page):
    page.goto("/index.html")
    expect(page.get_by_test_id("welcome-message")).to_be_visible()
```

## R4 — Locators só nos page objects *(verificada)*

Page objects expõem métodos com intenção (`sign_in`, `error_message`) e
devolvem valores ou outras pages, nunca elementos crus.

Correto:

```python
class LoginPage(BasePage):
    @property
    def _error(self):
        return self.page.get_by_test_id("login-error")

    def error_message(self) -> str:
        return self.text_of(self._error)
```

Incorreto:

```python
class AuthFlow:
    def error(self):
        return self._page.locator("#error")  # locator fora da page
```

## R5 — Prioridade de locators

1. Papel ou label acessível: `get_by_role`, `get_by_label`.
2. Atributo de teste: `get_by_test_id` (`data-testid`).
3. Seletor CSS.

XPath só com um comentário justificando.

Correto:

```python
self.page.get_by_role("button", name="Sign in")
```

Incorreto:

```python
self.page.locator("//div[3]/form/button[@class='btn btn-primary']")
```

## R6 — Esperas explícitas, nunca `time.sleep` *(verificada)*

Toda interação espera por uma condição, limitada pelo timeout de
`TIMEOUT_MS`. Se o timeout estourar, o erro do Playwright informa o locator e
o tempo de espera.

Correto:

```python
def welcome_message(self) -> str:
    return self.text_of(self._welcome)  # espera ficar visível
```

Incorreto:

```python
time.sleep(5)
return self.page.inner_text("h1")
```

## R7 — Nunca engolir exceções *(verificada)*

Uma falha de interação precisa falhar o teste.

Correto:

```python
self.click(self._sign_in_button)
```

Incorreto:

```python
try:
    self.click(self._sign_in_button)
except Exception:
    pass
```

## R8 — Asserções só nos test scripts *(verificada)*

Pages, flows e core devolvem valores; quem decide se passou é o teste.

Correto:

```python
assert login_page.heading() == "Sign in"
```

Incorreto:

```python
class LoginPage(BasePage):
    def check_heading(self):
        assert self.heading() == "Sign in"
```

## R9 — Dados de teste vêm de fixtures, sem hardcoding

Credenciais e dados saem da configuração ou de `business/data/`, entregues
por fixtures. Nada de literais repetidos entre testes.

Correto:

```python
def test_login_with_valid_credentials_shows_welcome_message(auth_flow, valid_user): ...
```

Incorreto:

```python
auth_flow.login_as(User("demo", "demo-password"))
```

## R10 — Testes independentes *(verificada)*

Nenhum teste depende da ordem de execução ou do estado deixado por outro. A
suíte roda em ordem aleatória, e cada teste recebe um contexto de navegador
novo.

Correto: cada teste faz o próprio login pelo flow.

Incorreto: um teste de logout que conta com o login feito pelo teste
anterior.
