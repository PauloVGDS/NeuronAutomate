import requests


def sendCredits(code, credits):
    # URL da request
    url = f"https://nc2c3oo9ak.execute-api.us-east-1.amazonaws.com/prod/v1/colocar-credito/blips_{code}/{credits}"

    # Fazendo a request GET
    response = requests.get(url)

    # Verificando se a request foi bem-sucedida
    if response.status_code == 200:
        print("\033[1;32m[✔] Créditos enviados com sucesso.\033[m")
        return True
    else:
        print(f'\033[1;33mErro na requisição: {response.status_code}\033[m')
        return False

#sendCredits("", 30)