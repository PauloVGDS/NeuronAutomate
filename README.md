# NeuronAutomate
- Automatizar o teste dos neurônios(ESP8266).
  - Conexão na rede do neurônio
  - Conexão do neurônio na rede
  - Envio de créditos ao neurônio
  - Envio do código do neurônio para planilha

# Tecnologias Usadas:
**Selenium**
- Usado para abrir o navegador, entrar no IP, inserir as informações da rede e conectar o neurônio.

**Google Sheets API**
- Usado para definir as credenciais e permitir acesso e armazenar o código do neurônio na planilha.

**Subprocess**
- Usado para executar os comandos Shell e armazenar os seus outputs.

**XML**
- Conectar em uma rede necessita de um perfil de rede, logo para cada conexão alteramos o arquivo XML e o usamos como perfil para conectar na rede.

**Requests**
- Lib usada para fazer a solicitação da API do Grafana para enviar os créditos ao neurônio.

**Arquivo .bat**
-  Serve para executar o código de maneira fácil.

**Em breve**
- Utilização do Flask e Electron.js para criação de uma interface.
