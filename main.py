import os
import subprocess
from xmlChange import changeXML
from googleSheets import insertValues

# Executar o comando e armazenar o resultado
networks = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)
networks = networks.stdout.split("\n")


# Filtar as informações importantes
networks = list(filter(lambda x: x.startswith("SSID"), networks))
neuronios = list()
# Iterando sobre as redes
for net in networks:
    # Adicionando na lista os neurônios
    if "blips_" in net:
        neuronios.append(net[-12:])


# Para cada neurônio:
for cod in neuronios:
    # Mudar o perfil
    changeXML(cod, "index.xml")
    # Adicionar o perfil
    os.system(f"netsh wlan add profile filename=index.xml")
    # Conectar na rede do neurônio
    os.system(f"netsh wlan connect {cod}")
    # Conectar o neurônio na rede

    # Enviar Créditos

    # Adicionar na Planilha
    insertValues(cod, "Teste")
    
    
