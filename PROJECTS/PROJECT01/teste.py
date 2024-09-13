import requests
import pandas as pd
import json

url = "http://app.omie.com.br/api/v1/geral/bancos/"

payload = {
    "call": "ListarBancos",
    "app_key": "SUA_APP_KEY_AQUI",
    "app_secret": "SEU_APP_SECRET_AQUI",
    "param": [
        {
            "pagina": 1,
            "registros_por_pagina": 100,
            "apenas_importado_api": "N"
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

# Supondo que a resposta JSON tenha uma estrutura que contém uma lista de bancos
# Adapte o caminho para acessar a lista correta conforme a estrutura da resposta
bancos = data.get('bancos', [])  # Substitua 'bancos' pelo nome correto se necessário

# Cria um DataFrame a partir da lista de bancos
df = pd.DataFrame(bancos)

# Exibe o DataFrame como uma tabela
print(df)
