from steps.utils import Utils
from pages.mapeamento import Map    


class Geral:
    def acessar_url(context,url):
        context.browser.get(url)
        context.browser.maximize_window() 

    def login(context,documento,senha):
        Utils.find_and_send(context,Map.LOC_DOCUMENTO,documento)
        Utils.find_and_click(context,Map.LOC_BOTAO_ENTRAR)
        Utils.find_and_send(context,Map.LOC_SENHA,senha)
        Utils.find_and_click(context,Map.LOC_CONTINUAR) 

    def recusar_modais(context):
        Utils.find_and_click(context,Map.LOC_ACEITAR_COOKIES)
        Utils.find_and_click(context,Map.LOC_PESQUISA)
        Utils.find_and_click(context,Map.LOC_TOUR_GUIADO)
        Utils.find_and_click(context,Map.LOC_AVISO)
        Utils.find_and_click(context,Map.LOC_MODAL_MODELO)

    def acessou(context):
        Utils.find_and_click(context,Map.LOC_TITULO_TOTAL)