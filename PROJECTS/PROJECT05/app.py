import requests
import pandas as pd
import ssl

def main(cont, key, secret):
    body = {
        "call": "ListarContasReceber",
        "app_key": key,
        "app_secret": secret,
        "param": [{   
            "filtrar_por_registro_de": "01/01/2024",
            "pagina": cont,
            "registros_por_pagina": 500,
            "apenas_importado_api": "N"
        }]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://app.omie.com.br/api/v1/financas/contareceber/",
            headers=headers,
            json=body,
            timeout=30,
            verify=False  # Disable SSL verification
        )

        if response.status_code == 200:
            data = response.json()
            conta_pagar_cadastro = data.get('conta_receber_cadastro', [])
            df = pd.json_normalize(conta_pagar_cadastro)
            return df
        else:
            print(f"Erro na requisição: {response.status_code}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# CHAMA O MAIN
cont = 1
resultados = []

data = {
    'Site': {'call': 'ListarContasReceber', 'app_key': '1102005564660', 'app_secret': 'd58d70a49a3f5b3f536057d14c63fa4b'}, #36
    'Itamar': {'call': 'ListarContasReceber', 'app_key': '1102013231319', 'app_secret': '2a332290a6173c88128adf1d7e31f4f9'}, #223
    'Gráfica Educa': {'call': 'ListarContasReceber', 'app_key': '3165494501169', 'app_secret': '59919980813d7bd18f89104852eeade6'}, #10
    'CDG': {'call': 'ListarContasReceber', 'app_key': '1102036231296', 'app_secret': '9cf2dd9c9b2b1c714d3c9ee792f296ed'}, #20
    'Benjamin': {'call': 'ListarContasReceber', 'app_key': '1101921231411', 'app_secret': 'd69170e421eef351ca95ddd7fc390a5b'}, #200
    
    
}


info = data['Benjamin']
key = info['app_key']
secret = info['app_secret']
NumeroQtde = 200

for i in range(NumeroQtde):
    print(f"Processando página {cont}...")
    df = main(cont, key, secret)
    if not df.empty:
        resultados.append(df)
    cont += 1

if resultados:
    df_final = pd.concat(resultados, ignore_index=True)
    df_final.to_csv("Dados/contas_receber_omie.csv", index=False)
    print("Todos os dados foram salvos no arquivo 'contas_receber_omie.csv'.")
else:
    print("Nenhum dado foi retornado.")
