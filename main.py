import os
import subprocess
from xmlChange import changeXML
from googleSheets import insertValues

# Executar o comando e armazenar o resultado
networks = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)
networks = networks.stdout.split("\n")


# Filtar as informações importantes
networks = list(filter(lambda x: x.startswith("SSID"), networks))
# Iterando sobre as redes
for net in networks:
    # Adicionando na lista os neurônios
    if "blips_" in net:
        neuronio = net[-12:]

    # Mudar o perfil
    changeXML(neuronio, "index.xml")
    # Adicionar o perfil
    os.system(f"netsh wlan add profile filename=index.xml")
    # Conectar na rede do neurônio
    os.system(f"netsh wlan connect {neuronio}")
    # Conectar o neurônio na rede

    # Enviar Créditos

    # Adicionar na Planilha
    insertValues(neuronio, "Teste")
    
    
