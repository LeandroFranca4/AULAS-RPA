from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

chrome_options= Options()

arguments= ['--lang=pt-BR', '--window-size=800,600','--incognito']

'''COMMON ARGUMENTS
--start-maximized #inicia maximizado
--lang=pt-BR #define idioma de inicialização
--incoginto #usa o modo anônimo
--window-size=800,800 #define a resolução da janela em largura e altura
--disable-notifications # Desabilita notificações
--disable-gpu # desabilita renderização com GPU'''
#iniciando o wbdriver

for argument in arguments:
    chrome_options.add_argument(argument)

caminho_padrao_para_download = 'C:\oloco'
# Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
# Uso de configurações experimentais
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'C:\oloco',
    #
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,

})
# inicializando o webdriverS
driver = webdriver.Chrome( options=chrome_options)
# Navegar até um site

driver.get('https://cursoautomacao.netlify.app/desafios')

driver.execute_script('window.scrollTo(0,1900)')
sleep(1)


caixa= driver.find_elements(By.XPATH,"//input[@name='motos']")
for moto in caixa:
    moto.click()









input('')
driver.close()