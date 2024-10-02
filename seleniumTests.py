# Importações da lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


## Seleção do Driver
#driver = webdriver.Chrome()
#
#
## Acesso a URL
#driver.get("http://127.0.0.1:5000")
#
## Seleção dos inputs
#text_box = driver.find_element(by=By.TAG_NAME, value="h1")
#input_box = driver.find_element(By.ID, "network")
#submit_btn = driver.find_element(By.TAG_NAME, value="button")
#
#
## Inserção dos valores / Inserir o link
#input_box.send_keys("Paulo")
#submit_btn.click()
#
## Timer
#driver.implicitly_wait(0.5)
#
## Timer condicional
#WebDriverWait(driver, 5).until(
#    expected_conditions.presence_of_element_located((By.CLASS_NAME, "teste"))
#)
#
## Inserção de valores e pressionar tecla Enter
#input_box.send_keys("Pedro" + Keys.ENTER)
#
#
## Mensagem de Sucesso/Falha
#text_box = driver.find_element(By.ID, "title")
#print(text_box.text)
#driver.get("http://127.0.0.1:5000/after")
#
#
## Saindo do driver
#driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def connectNeuron():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu") 
    # Seleção do Driver
    driver = webdriver.Chrome(options=chrome_options)

    # Acesso a URL
    driver.get("http://192.168.4.1/wi?s1=Pedro&p1=91204673&save=")
    time.sleep(10)
    # Saindo do driver
    driver.quit()
    return "Neurônio conectado com sucesso."