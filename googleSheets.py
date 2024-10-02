import gspread
from google.oauth2.service_account import Credentials
import os

DIR = os.path.dirname(os.path.realpath(__file__))

def insertValues(cod, worksheet):
    # Carregar as credenciais
    credentials = Credentials.from_service_account_file(
        rf'{DIR}\config\apiCredential.json',
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

    return print("Planilha atualizada com sucesso!")

#insertValues("blips_FFFFFF", "Teste")
