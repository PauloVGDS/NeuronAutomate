import gspread
from google.oauth2.service_account import Credentials


def sheetConnect():
    try:
        # Carregar as credenciais
        credentials = Credentials.from_service_account_file(
            rf'.\config\apiCredential.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )

        # Autenticação
        gc = gspread.authorize(credentials)

        # Acessar a planilha pelo ID
        spreadsheet = gc.open_by_key('1sFqXEoL1KiW0Hb5lzcq55w61oTkcY1ZZPmn-uvWgwTo')
        print(f"[✔] Planilha Conectada!")
        return spreadsheet
    except Exception as e:
        print(f"Erro ao conectar na planilha: {e}")
        return False


def insertValues(cod, worksheet):
    try:

        spreadsheet = sheetConnect()
        # Selecionar a aba
        worksheet = spreadsheet.worksheet(worksheet)

        # Adicionar valores em uma linha específica
        worksheet.append_row([cod])
        print("[✔] Planilha atualizada com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro ao adicionar na planilha: {e}")
        return False


def getWorksheets():
    spreadsheet = sheetConnect()
    exclude = ["Status cores planilha", "Máquinas enviadas sem neurônio", "Duplicado" ,"Defeitos"]
    worksheets = []
    for sheet in spreadsheet.worksheets():
        if sheet.title not in exclude:
            worksheets.append(sheet.title)
            
    return worksheets

if __name__ == "__main__":
    getWorksheets()