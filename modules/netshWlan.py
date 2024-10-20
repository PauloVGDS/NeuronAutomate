import subprocess
from time import sleep

def findNetwork():
    
    try:
        # Armazena as redes encontradas
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
            print(f"Neurônio: {neuronio} encontrado com sucesso!")
            return neuronio
        print("Rede não encontrada!")
        return False
    except Exception as e:
        print(f"Rede não encontrada: {e}!")
        return False

def searchNetwork():
    try:
        # Procurar pelas redes por perto
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"], shell=True)
        sleep(2)
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"], shell=True)
        return True
    except Exception as e:
        print(f"Erro: {e}!")
        return False
    finally:
        subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"], shell=True)
        
def connectNetwork(net, file="index.xml", new=True):
    
    try:
        # Condição para conexões novas
        if new:
            directory = fr".\templates\{file}"
            subprocess.run(['netsh', 'wlan', 'add', 'profile', fr'filename={directory}'], check=True,)
        subprocess.run(['netsh', 'wlan', 'connect', f'name={net}'], check=True,)
        print(f"[✔] Pedido de conexão para {net} enviado!")
        return True
    except Exception as e:
        print(f"Erro ao conectar na rede: {e}")
        return False

if __name__ == "__main__":
    searchNetwork()
    connectNetwork("blips-CD9EEA-3818")
