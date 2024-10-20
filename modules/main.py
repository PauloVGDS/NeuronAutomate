import modules as md
from time import sleep


def completeTest(net, password, worksheet, creditos=30):
    try:
        # Busca as redes disponíveis ao redor
        neuronio = md.findNetwork()
        while not neuronio:
            md.searchNetwork()
            sleep(2)
            neuronio = md.findNetwork()
        # Mudar o perfil
        if not md.changeXML(neuronio, "index.xml"):
            raise Exception
        # Conectar na rede do neurônio
        if not md.connectNetwork(neuronio):
            raise Exception
        sleep(5)
        # Conectar o neurônio na rede
        if not md.connectNeuron(net, password):
            raise Exception
        # Conectar na rede anterior
        if not md.connectNetwork(net, new=False):
            raise Exception
        sleep(5)
        # Adicionar na Planilha
        #print("Onde deseja salvar?")
        #aba = input("Nome da aba:")
        if not md.insertValues(neuronio[6:12], worksheet):
            raise Exception
        # Enviar Créditos
        if not md.sendCredits(neuronio[6:12], creditos):
            raise Exception
        
        return True
    except Exception as e:
        print(e)
        return False
    
    
if __name__ == "__main__":
    completeTest("IDEAL", "Blips1521", "CNC 6040")
    # Informações dinâmicas:
    # Rede de conexão
    # Planilha de armazenamento
    # Créditos(padrão=30)