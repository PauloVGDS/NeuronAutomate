import xml.etree.ElementTree as ET
from googleSheets import DIR

def changeXML(cod, file="index.xml"):
    try:
        # Carregar o arquivo XML
        tree = ET.parse(rf"{DIR}\templates\{file}")
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
        tree.write(rf"{DIR}\templates\{file}", encoding='utf-8', xml_declaration=True)
        print("\033[1;32m[✔] Arquivo XML alterado com sucesso.\033[m")
        return True
    except Exception as e:
        print(f"\033[1;31mErro a alterar o arquivo XML: \033[1;33m{e}\033[m")
        return False
#changeXML("blips_FFaFFF", "index.xml")