import requests


def sendCredits(code, credits):
    # URL da request
    url = f"https://nc2c3oo9ak.execute-api.us-east-1.amazonaws.com/prod/v1/colocar-credito/blips_{code}/{credits}"

    # Fazendo a request GET
    response = requests.get(url)

    # Verificando se a request foi bem-sucedida
    if response.status_code == 200:
        print("[✔] Créditos enviados com sucesso.")
        return True
    else:
        print(f'Erro na requisição: {response.status_code}')
        return False

#sendCredits("", 30)