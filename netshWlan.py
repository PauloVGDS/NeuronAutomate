from googleSheets import DIR
import subprocess

def searchNetwork():
    # Procurar pelas redes por perto
    networks = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)
    # Pega o resultado do comando e divide em uma lista
    networks = networks.stdout.split("\n")
    # Filtra o resultado para apenas o nome das conexões
    networks = list(filter(lambda x: x.startswith("SSID"), networks))
    neuronio = ""
    # Loop pelas redes
    for net in networks:
    # Condição para retornar o código da rede com o prefixo
        if "blips-" in net:
            neuronio = net[-17:]
            return neuronio


def connectNetwork(net, file="index.xml", new=True):
    # Condição para conexões novas
    if new:
        directory = fr"{DIR}\{file}"
        subprocess.run(['netsh', 'wlan', 'add', 'profile', fr'filename={directory}'], check=True,)
    subprocess.run(['netsh', 'wlan', 'connect', f'name={net}'], check=True,)
    return print(f"[✔] Rede {net} Conectada")

#print(findCode()[6:])
#connectNetwork("blips-CD9EEA-3818")
