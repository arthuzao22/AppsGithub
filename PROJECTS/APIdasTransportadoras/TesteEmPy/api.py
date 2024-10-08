import requests
import base64

# Substitua pelos seus valores de login e senha
username = '25370117000198'
password = 'Cdg102030'
authorization_basic = base64.b64encode(f'{username}:{password}'.encode()).decode()  # Codificando em Base64
print(authorization_basic)
# URL da API, substitua pelos valores corretos de CNPJ e Nota Fiscal
url = 'https://api.braspress.com/v1/tracking/25370117000198/15288/json'

# Configurando os cabeçalhos da requisição
headers = {
    'Authorization': f'Basic {authorization_basic}',  # Insere a autenticação
    'Content-Type': 'application/json; charset=utf-8',
}

# Fazendo a requisição GET
try:
    response = requests.get(url, headers=headers)

    # Verificando o status da resposta
    response.raise_for_status()  # Levanta um erro para códigos de status 4xx ou 5xx
    result = response.json()  # Obtém o resultado no formato JSON
    print(result)  # Manipule o resultado conforme necessário

except requests.exceptions.HTTPError as err:
    print(response.text)  # Para ver a resposta em texto
except Exception as e:
    print(f'Outro erro: {e}')  # Exibe outros erros
