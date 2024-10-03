import time
from xmlChange import changeXML
from googleSheets import insertValues
from netshWlan import searchNetwork, connectNetwork
from seleniumTests import connectNeuron
from requestsConnection import sendCredits

def completeTest():
    try:
        # Busca as redes disponíveis ao redor
        neuronio = searchNetwork()
        # Mudar o perfiltime.sleep(5)
        changeXML(neuronio, "index.xml")
        # Conectar na rede do neurônio
        connectNetwork(neuronio)
        time.sleep(5)
        # Conectar o neurônio na rede
        connectNeuron()
        # Conectar na rede anterior
        time.sleep(10)
        connectNetwork("BLIPS", new=False)
        time.sleep(10)
        # Enviar Créditos
        sendCredits(neuronio[6:12], 30)
        # Adicionar na Planilha
        #print("Onde deseja salvar?")
        #aba = input("Nome da aba:")
        insertValues(neuronio[6:12], "")
    except Exception as e:
        return print(e)
    
if __name__ == "__main__":
    completeTest()

#http://192.168.4.1/wi?s1=BLIPS&p1=Blips1521&save=    
