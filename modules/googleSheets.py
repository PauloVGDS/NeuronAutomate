import gspread
from google.oauth2.service_account import Credentials
import os

DIR = os.path.dirname(os.path.realpath(__file__))

def insertValues(cod, worksheet):
    try:
        # Carregar as credenciais
        credentials = Credentials.from_service_account_file(
            rf'{DIR}\config\apiCredential.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

        # Autenticação
        gc = gspread.authorize(credentials)

        # Acessar a planilha pelo ID
        spreadsheet = gc.open_by_key('1sFqXEoL1KiW0Hb5lzcq55w61oTkcY1ZZPmn-uvWgwTo')

        # Selecionar a aba
        worksheet = spreadsheet.worksheet(worksheet)

        # Adicionar valores em uma linha específica
        worksheet.append_row([cod])
        print("\033[1;32m[✔] Planilha atualizada com sucesso!\033[m")
        return True
    
    except Exception as e:
        print(f"\033[1;31mErro ao adicionar na planilha: \033[1;33m{e}\033[m")
        return False
