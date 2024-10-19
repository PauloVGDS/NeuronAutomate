from time import sleep
from xmlChange import changeXML
from googleSheets import insertValues
from netshWlan import findNetwork, connectNetwork, searchNetwork
from seleniumTests import connectNeuron
from requestsConnection import sendCredits

def completeTest(net, password, worksheet, creditos=30):
    try:
        # Busca as redes disponíveis ao redor
        neuronio = findNetwork()
        while not neuronio:
            searchNetwork()
            neuronio = findNetwork()
        # Mudar o perfil
        if not changeXML(neuronio, "index.xml"):
            raise Exception
        
        # Conectar na rede do neurônio
        if not connectNetwork(neuronio):
            raise Exception
        sleep(5)
        # Conectar o neurônio na rede
        if not connectNeuron(net, password):
            raise Exception
        # Conectar na rede anterior
        if not connectNetwork(net, new=False):
            raise Exception
        sleep(5)
        # Adicionar na Planilha
        #print("Onde deseja salvar?")
        #aba = input("Nome da aba:")
        if not insertValues(neuronio[6:12], worksheet):
            raise Exception
        # Enviar Créditos
        if not sendCredits(neuronio[6:12], creditos):
            raise Exception
    except Exception as e:
        return print(e)
    
    
if __name__ == "__main__":
    completeTest("IDEAL", "Blips1521", "CNC 6040")
    # Informações dinâmicas:
    # Rede de conexão
    # Planilha de armazenamento

#http://192.168.4.1/wi?s1=&p1=&save=    