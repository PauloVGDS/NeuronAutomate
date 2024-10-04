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
        if not neuronio:
            raise Exception
        # Mudar o perfiltime.sleep(5)
        if not changeXML(neuronio, "index.xml"):
            raise Exception
        
        # Conectar na rede do neurônio
        if not connectNetwork(neuronio):
            raise Exception
        time.sleep(5)
        # Conectar o neurônio na rede
        if not connectNeuron():
            raise Exception
        # Conectar na rede anterior
        if not connectNetwork("BLIPS", new=False):
            raise Exception
        time.sleep(5)
        # Adicionar na Planilha
        #print("Onde deseja salvar?")
        #aba = input("Nome da aba:")
        if not insertValues(neuronio[6:12], "Simulador de Escada"):
            raise Exception
        # Enviar Créditos
        if not sendCredits(neuronio[6:12], 30):
            raise Exception
    except Exception as e:
        return print(e)
    
    
if __name__ == "__main__":
    completeTest()

#http://192.168.4.1/wi?s1=BLIPS&p1=Blips1521&save=    
