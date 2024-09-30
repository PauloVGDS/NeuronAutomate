import gspread
from google.oauth2.service_account import Credentials

def insertValues(cod, worksheet):
    # Carregar as credenciais
    credentials = Credentials.from_service_account_file(
        rf'F:\main\config\apiCredential.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    # Autenticação
    gc = gspread.authorize(credentials)

    # Acessar a planilha pelo ID
    spreadsheet = gc.open_by_key('1yQHRiSyQi8WKiyfTxjSN2NPOwFM3hMtjHJ4WZ5L5_D8')

    # Selecionar a aba
    worksheet = spreadsheet.worksheet(worksheet)

    # Adicionar valores em uma linha específica
    worksheet.append_row([cod])

    return print("Valores adicionados com sucesso!")
