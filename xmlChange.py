import xml.etree.ElementTree as ET
from googleSheets import DIR

def changeXML(cod, file):
    
    # Carregar o arquivo XML
    tree = ET.parse(rf"{DIR}\{file}")
    root = tree.getroot()

    # Definir o namespace (se necessário)
    ns = {'ns': 'http://www.microsoft.com/networking/WLAN/profile/v1'}

    # Alterar o valor do elemento <name> dentro do <WLANProfile>
    ssid_element = root.find('ns:name', ns)
    if ssid_element is not None:
        ssid_element.text = cod

    # Alterar o valor do elemento <name> dentro do <SSID>
    ssid_element = root.find('ns:SSIDConfig/ns:SSID/ns:name', ns)
    if ssid_element is not None:
        ssid_element.text = cod

    # Salvar as alterações no arquivo XML
    tree.write(rf"{DIR}\{file}", encoding='utf-8', xml_declaration=True)

    return print("[✔] Arquivo XML alterado com sucesso.")

#changeXML("blips_FFaFFF", "index.xml")