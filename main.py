import time
from xmlChange import changeXML
from googleSheets import insertValues, DIR
from netshWlan import findCode, connectNetwork
from seleniumTests import connectNeuron
from requestsConnection import sendCredits

def completeTest():
    try:
        neuronio = findCode()
        # Mudar o perfiltime.sleep(5)
        changeXML(neuronio, "index.xml")
        # Conectar na rede do neurônio
        connectNetwork(neuronio)
        time.sleep(5)
        # Conectar o neurônio na rede
        connectNeuron()
        # Conectar na rede anterior
        time.sleep(5)
        connectNetwork("BLIPS", new=False)
        time.sleep(5)
        # Enviar Créditos
        sendCredits(neuronio[6:12], 30)
        # Adicionar na Planilha
        insertValues(neuronio[:12], "Teste")
    except Exception as e:
        return print(e)
    
if __name__ == "__main__":
    completeTest()

#http://192.168.4.1/wi?s1=Pedro&p1=91204673&save=    
