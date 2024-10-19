# Importações da lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Código de Estudo
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
#input_box.send_keys("BLIPS")
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
#input_box.send_keys("BLIPS" + Keys.ENTER)
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


def connectNeuron(): 
    try:
        # Seleção do Driver
        driver = webdriver.Chrome()

        # Acesso a URL
        driver.get("http://192.168.4.1/wi?s1=IDEAL&p1=Blips1521&save=")
        # Timer condicional
        WebDriverWait(driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Conexão WiFi bem-sucedida']"))
        )
        #<div style="text-align:center;color:#008000;">Conexão WiFi bem-sucedida<br><br></div>
        # Saindo do driver
        driver.quit()
        print("\033[1;32m[✔] Neurônio conectado com sucesso.\033[m")
        return True
    except Exception as e:
        print(f"\033[1;31mErro ao conectar o neurônio: \033[1;33m{e}\033[m")
        
#connectNeuron()