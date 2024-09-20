from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #como o navegador irá se comportar
import time
import os #operações de arquivos com python

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.prompt_for_download': False, #permite a aprovação automática do donwlaod sem que precise aprovar
    'download.default_directory': r'D:\Workspace programming\Python\RPA_LEARN\01_RPA\relatorios', #coloca todos os downloads neste diretório 
    'profile.default_content_setting_values.automatic_downloads': 1, #não pedi permissão para realizar múltiplos downloads
})

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://consulta-empresa.netlify.app')

time.sleep(3)

driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/form/div[1]/input').send_keys('jhonatan')
driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/form/div[2]/input').send_keys('12345678')
driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/form/div[3]/button').click()

time.sleep(3)

def baixar_relatorios_das_empresas(driver):
    nomes_empresas = driver.find_elements(By.XPATH, "//td[@name='nome_empresa']")
    time.sleep(2)
    botoes_download_pdf = driver.find_elements(By.XPATH, "//button[@class='download-btn']")
    time.sleep(2)


    #laço de repetição para cada elemento
    #o zip permite iterar em mais de uma lista
    for nome, botao_pdf in zip(nomes_empresas, botoes_download_pdf):
        botao_pdf.click()
        time.sleep(2)
        #renomear arquivo de perfil_empresa (padrão) para nome da empresa
        diretorio = r'D:\Workspace programming\Python\RPA_LEARN\01_RPA\relatorios'
        nome_antigo_arquivo = 'perfil_empresa.pdf'
        novo_nome = f'{nome.text}.pdf'

        #MONTANDO O CAMINHO COMPLETO PARA RENOMAER
        caminho_completo_antigo = os.path.join(diretorio, nome_antigo_arquivo)
        caminho_completo_novo = os.path.join(diretorio, novo_nome)

        #RENOMEANDO ARQUIVOS
        os.rename(caminho_completo_antigo, caminho_completo_novo)


baixar_relatorios_das_empresas(driver=driver)
botao_proxima_pagina = driver.find_element(By.XPATH, "//button[@id='nextBtn']")
while botao_proxima_pagina.get_attribute('disabled') == None:
    botao_proxima_pagina.click()
    baixar_relatorios_das_empresas(driver=driver)

input('Aperte ENTER para finalizar.')