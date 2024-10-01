import os
from xmlChange import changeXML
from googleSheets import insertValues, DIR
from netshWlan import findCode

neuronio = findCode()
# Mudar o perfil
changeXML(neuronio, "index.xml")
# Adicionar o perfil
os.system(rf'netsh wlan add profile filename="{DIR}\index.xml"')
# Conectar na rede do neurônio
os.system(f'netsh wlan connect "{neuronio}"')
# Conectar o neurônio na rede

# Enviar Créditos

# Adicionar na Planilha
#insertValues(neuronio, "Teste")
    
    
