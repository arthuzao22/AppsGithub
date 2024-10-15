import requests
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main(cont, key, secret, call_type):
    body = {
        "call": call_type,
        "app_key": key,
        "app_secret": secret,
        #"filtrar_por_registro_de": "02/06/2024",
        "param": [{
            "pagina": cont,
            "registros_por_pagina": 500,
            "apenas_importado_api": "N"
        }]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(
            "https://app.omie.com.br/api/v1/financas/contapagar/",
            headers=headers,
            json=body,
            timeout=30,
            verify=False
        )

        data = response.json()
        print(f"Resposta da API (página {cont}): {data}")

        if response.status_code == 200 and 'conta_pagar_cadastro' in data:
            conta_cadastro = data['conta_pagar_cadastro']
            df = pd.json_normalize(conta_cadastro)
            return df
        else:
            print(f"Erro na resposta: {response.status_code} - {data}")
            return pd.DataFrame()

    except requests.exceptions.Timeout:
        print("A requisição expirou.")
        return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return pd.DataFrame()
    except ValueError:
        print("Erro ao processar a resposta JSON.")
        return pd.DataFrame()

# CHAMA O MAIN
cont = 1
resultados = []

info = {
    'call': 'ListarContasPagar',
    'app_key': '1102036231296',
    'app_secret': '9cf2dd9c9b2b1c714d3c9ee792f296ed'
}
key = info['app_key']
secret = info['app_secret']
call_type = info['call']

NumeroQtde = 40

for i in range(NumeroQtde):
    print(f"Processando página {cont}...")
    df = main(cont, key, secret, call_type)
    if not df.empty:
        resultados.append(df)
    cont += 1

if resultados:
    df_final = pd.concat(resultados, ignore_index=True)
    df_final.to_csv("Dados/contas_receber_omie.csv", index=False)
    print("Todos os dados foram salvos no arquivo 'contas_receber_omie.csv'.")
else:
    print("Nenhum dado foi retornado.")
