from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import *
import yaml
import os
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from behave import fixture

def before_all(context):
    # Carregue as variáveis do arquivo YAML
    with open('config.yml', 'r') as file:
        context.config_data = yaml.safe_load(file)

browserstack = False
execution_number = 1  # Inicializa o número da execução

def before_scenario(context, scenario):
    global execution_number

    # Cria uma pasta para a execução atual
    context.screenshot_folder = f'images/teste_execucao_{execution_number}'

    # Incrementa o número da execução se a pasta já existir
    while os.path.exists(context.screenshot_folder):
        execution_number += 1
        context.screenshot_folder = f'images/teste_execucao_{execution_number}'

    os.makedirs(context.screenshot_folder)
    
    if browserstack:    
        desired_capabilities = {
            'browserName': 'chrome'
        }
        context.browser = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            # command_executor="http://localhost:4444/wd/hub"
        )
        
        context.browser.delete_all_cookies()
        context.browser.maximize_window()
    else:
        context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        context.browser.delete_all_cookies()
        context.browser.maximize_window()
    # else:
    #     service = Service('drivers\chromedriver.exe')
    #     context.browser = webdriver.Chrome(service=service)
    #     context.browser.delete_all_cookies()
    #     context.browser.maximize_window()

def after_step(context, step):
    # Tire um screenshot após cada step, independentemente de passar ou falhar
    step_name = step.name.replace(' ', '_')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_path = f'{context.screenshot_folder}/{step_name}_{timestamp}.png'
    context.browser.save_screenshot(screenshot_path)
    print(f'Screenshot salvo em: {screenshot_path}')

    # Se o step falhar, renomeie o arquivo para 'defeito'
    if step.status == 'failed':
        new_path = f'{context.screenshot_folder}/defeito_{timestamp}.png'
        os.rename(screenshot_path, new_path)
        print(f'Screenshot renomeado para: {new_path}')

def after_scenario(context, scenario):
    context.browser.quit()
