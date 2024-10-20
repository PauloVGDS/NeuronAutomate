import xml.etree.ElementTree as ET


def changeXML(cod, file="index.xml"):
    try:
        # Carregar o arquivo XML
        tree = ET.parse(rf".\templates\{file}")
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
        tree.write(rf".\templates\{file}", encoding='utf-8', xml_declaration=True)
        print("[✔] Arquivo XML alterado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro a alterar o arquivo XML: {e}")
        return False

if __name__ == "__main__":
    changeXML("blips_FFaFFF", "index.xml")