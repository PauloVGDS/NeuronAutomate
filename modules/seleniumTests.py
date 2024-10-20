# Importações da lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


async def connectNeuron(): 
    try:
        # Seleção do Driver
        driver = webdriver.Chrome()
        # Acesso a URL
        await driver.get("http://192.168.4.1/wi?s1=IDEAL&p1=Blips1521&save=")
        # Timer condicional
        WebDriverWait(driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Conexão WiFi bem-sucedida']"))
        )
        # Saindo do driver
        driver.quit()
        print("\033[1;32m[✔] Neurônio conectado com sucesso.\033[m")
        return True
    except Exception as e:
        print(f"\033[1;31mErro ao conectar o neurônio: \033[1;33m{e}\033[m")
        
        

if __name__ == "__main__":
    connectNeuron()