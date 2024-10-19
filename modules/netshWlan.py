from googleSheets import DIR
import subprocess

def searchNetwork():
    
    try:
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
        if neuronio != "":
            print(f"\033[1;32mNeurônio: {neuronio} encontrado com sucesso!\033[m")
            return neuronio
        print("\033[1;31mRede não encontrada!\033[m")
        return False
    except Exception as e:
        print(f"\033[1;31mRede não encontrada: {e}!\033[m")
        return False


def connectNetwork(net, file="index.xml", new=True):
    # Condição para conexões novas
    try:
        if new:
            directory = fr"{DIR}\templates\{file}"
            subprocess.run(['netsh', 'wlan', 'add', 'profile', fr'filename={directory}'], check=True,)
        subprocess.run(['netsh', 'wlan', 'connect', f'name={net}'], check=True,)
        print(f"\033[1;32m[✔] Pedido de conexão para {net} enviado!\033[m")
        return True
    except Exception as e:
        print(f"\033[1;31mErro ao conectar na rede: \033[1;33m{e}\033[m")
        return False

#searchNetwork()
#connectNetwork("blips-CD9EEA-3818")
