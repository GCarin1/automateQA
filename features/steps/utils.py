import re
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
#from features.environment import browserstack
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Utils:
    
    def find_and_click(context, locator_generic, wait_time=60):
        try:
            element = WebDriverWait(context.browser, wait_time).until(EC.visibility_of_element_located(locator_generic))
            element.click()
        except TimeoutException as e:
            print(f"Elemento não encontrado dentro do tempo limite de {wait_time} segundos.")
        except Exception as e:
            print(f"Ocorreu um erro ao clicar no elemento: {e}")
    def find_and_send(context, locator_generic, text, wait_time=60):
            try:
                WebDriverWait(context.browser, wait_time).until(EC.visibility_of_element_located(locator_generic)).send_keys(text)
            except Exception as e:
                pass
    
    def substituir_mapeamento(context, locator, texto, regex='%.*%'):
        if isinstance(locator, tuple) and len(locator) == 2 and locator[0] == By.XPATH:
            xpath = locator[1]
            novo_locator = (By.XPATH, re.sub(re.escape(regex), texto, xpath))
            print(novo_locator)
            return novo_locator
        else:
            raise TypeError("O argumento 'locator' não é um objeto By com XPath.")

        #return locator
    def find_and_return_text(context, locator, wait_time=60):
        try:
            wait = WebDriverWait(context.browser, wait_time)
            element = None

            try:
                element = wait.until(EC.presence_of_element_located((locator)))
            except:
                element = wait.until(EC.presence_of_element_located((locator)))

            if element:
                element_text = element.text
                print(element_text)
            else:
                return None
        except Exception as e:
            print(f"Erro: {str(e)}")
            return None
    # def click_elemento(context,locator_generic):
    #     try:
    #         context.find_and_click(context, locator_generic)
    #     except:
    #         print(f'Não foi encontrado ou não é apresentado na versão mobile/desktop')
    
    # def limpar_campo(context, locator):
    #     context.webdriver.execute_script('arguments[0].value = "";', context.achar_elemento(locator))
    
    def achar_elemento(context, locator):
        try:
            return context.webdriver.find_element(*locator)
        except: 
            raise NoSuchElementException()
    def resolucao_notebook(context):
        context.webdriver.set_window_size(1382, 768)

    def resolucao_desktop(context):
        context.webdriver.set_window_size(1940, 1080)

    