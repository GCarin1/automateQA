from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import *
import yaml

def before_all(context):
    # Carregue as variáveis do arquivo YAML
    with open('config.yml', 'r') as file:
        context.config_data = yaml.safe_load(file)

browserstack=False
def before_scenario(context, scenario):
    if browserstack:    
        desired_capabilities = {
            'browserName': 'chrome'
        }
        context.browser = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            #command_executor="http://localhost:4444/wd/hub"
        )
        
        context.browser.delete_all_cookies()
        context.browser.maximize_window()
    else:
        service = Service('drivers\chromedriver.exe')
        context.browser = webdriver.Chrome(service=service)
        context.browser.delete_all_cookies()
        context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()
