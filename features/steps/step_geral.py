from behave import *
from pages.page_geral import Geral


@given('que eu esteja na pagina')
def step_user_on_login_page(context):
    url = context.config_data.get('url')
    Geral.acessar_url(context,url)

@when('faco login usando o documento')
def step_enter_valid_credentials(context):
    username = context.config_data.get('user01')
    password = context.config_data.get('password')

    Geral.login(context,username,password)


@when('Aceitar cookies e recusar pesquisa e tour')
def step(context):
    Geral.recusar_modais(context)

@then('acessou')
def step(context):
    Geral.acessou(context)
    