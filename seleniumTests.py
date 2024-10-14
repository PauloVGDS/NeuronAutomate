# Importações da lib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def connectNeuron(net, password): 
    try:
        # Seleção do Driver
        driver = webdriver.Chrome()

        # Acesso a URL
        driver.get(f"http://192.168.4.1/wi?s1={net}&p1={password}&save=")
        
        # Timer condicional
        WebDriverWait(driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Conexão WiFi bem-sucedida']"))
        )
        # Fechando o navegador
        driver.quit()
        print("[✔] Neurônio conectado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao conectar o neurônio: {e}")
        
if __name__ == "__main__":
    connectNeuron()