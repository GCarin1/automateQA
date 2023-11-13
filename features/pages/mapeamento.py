from selenium.webdriver.common.by import By

class Map:
    LOC_TESTE_TITULO=(By.XPATH,"(//h2[contains(text(),'Proventos')])[1]")
########## HOME ########################
    LOC_BOTOES_HOME=(By.XPATH,"//button[contains(text(),'%BUTTON_TEXT%')]")
    LOC_DATA_CARGA=(By.XPATH,"//p[@class='b3i-total-acumulado__disclaimer b3i-total-acumulado__card__aside__data']")
    LOC_TITULOS_HOME=(By.XPATH,"//h2[contains(text(),'%TITULO_HOME%')]")
    LOC_VALOR_TOTAL=(By.XPATH,"//h2[@class='b3i-total-acumulado__valor ng-star-inserted']")
    LOC_DISCLAIMER_TITULO=(By.XPATH,"//h2[@class='b3i-total-acumulado__disclaimer']")
    LOC_VISUALIZAR_POR=(By.XPATH,"//input[@value='%VISUALIZAR_GRAFICO%']")
    LOC_DETALHES_RV_RF=(By.XPATH,"(//button[@aria-label='%MAIS_DETALHE%'])[2]")
    LOC_DISCLAIMER_DETALHER_RV_RF=(By.XPATH,"(//p[@class='b3i-detalhes__texto'])[1]")
    LOC_X_FECHAR_DETALHER=(By.XPATH,"(//button[@aria-label='Fechar modal de detalhes'])")
    LOC_BOTAO_IR=(By.XPATH,"//button[@aria-label='%IR_PARA%']")
    #mapeamento unico mobile home
    LOC_DETALHES_HOME_MOB="(//span[contains(text(),'Detalhes')])[2]"
    LOC_REDIRECIONA_HOME_MOB="(//span[contains(text(),'%TITULO%')])[1]"
    LOC_RETORNAR_TOPO="//button[@class='b3-use-button b3-use-button-light b3-use-button-light--primary b3-use-button--default b3-ga-button b3-use-button--onlyIcon']"

    
########## GERAL #######################
    LOC_DOCUMENTO = (By.ID, "cpf_mask")
    LOC_SENHA = (By.ID, "PASS_INPUT")
    LOC_BOTAO_ENTRAR = (By.XPATH, "//span[contains(text(), 'Entrar')]")
    LOC_CONTINUAR = (By.ID, "Btn_CONTINUE")
    LOC_AVISO = (By.XPATH,"//button[@class='b3-botao b3-botao-light b3-botao-light--primary b3-botao--default b3-ga-button']")
    LOC_ACEITAR_COOKIES = (By.ID, "onetrust-accept-btn-handler")
    LOC_PESQUISA=(By.XPATH,"//button[contains(.,'×')]")
    LOC_TOUR_GUIADO = (By.ID, "btn-pular")
    LOC_MODAL_MODELO=(By.XPATH,"//span[contains(.,'Ok, entendi')]")
    LOC_TITULO_TOTAL=(By.XPATH,"//h1[contains(.,'Total Acumulado')]")
    
    #MENUS
    LOC_SELEC_MENU=(By.XPATH,"(//button[contains(.,'%SELECMENUS%')])[1]")
    LOC_MENU=(By.XPATH,"//button[contains(.,'Menu')]")

