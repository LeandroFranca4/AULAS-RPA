from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = iniciar_driver()

# navegar até o site
driver.get('https://cursoautomacao.netlify.app/')
sleep(6)
#Encontrar e clicar na area de desafios
botao_desafio = driver.find_element(By.XPATH,'//*[@id="navbarsExample04"]/ul[2]/li[2]/a')
botao_desafio.click()
sleep(3)
#Rolar o mouse para baixo
driver.execute_script("window.scrollTo(0, 850);")
sleep(4)
#Função de digitação
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

#Encontrando o campo de digitação
paragrafo = driver.find_element(By.XPATH,'//*[@id="campoparagrafo"]')
sleep(5)
texto = 'Colocando um evento aleatório para que se possa ser imprimido na tela'

digitar_naturalmente(texto,paragrafo)

input('')
driver.close()