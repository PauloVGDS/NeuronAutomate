import requests


def sendCredits(code, credits):
    url = f"https://nc2c3oo9ak.execute-api.us-east-1.amazonaws.com/prod/v1/colocar-credito/blips_{code}/{credits}"
    # Parâmetros de consulta (query parameters)

    # Fazendo a requisição GET com parâmetros
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        print("[✔] Créditos enviados com sucesso.")
        return True
    else:
        print(f'Erro na requisição: {response.status_code}')
        return False

#sendCredits("CD8FA7", 30)