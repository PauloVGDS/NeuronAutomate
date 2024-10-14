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
        print("[✔] Planilha atualizada com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro ao adicionar na planilha: {e}")
        return False
    

if __name__ == "__main__":
    insertValues("blips_FFFFFF", "Teste")