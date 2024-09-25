import requests
import pandas as pd

def main(cont):
    body = {
        "call": "ListarClientes",
        "app_key": "1102005564660",
        "app_secret": "d58d70a49a3f5b3f536057d14c63fa4b",
        "param": [{
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
            "https://app.omie.com.br/api/v1/geral/clientes/",
            headers=headers,
            json=body,
            timeout=30,
            verify=False  # Desativa a verificação SSL
        )

        if response.status_code == 200:
            data = response.json()
            print(data)  # Exibe a resposta completa da API para verificação
            clientes_list = data.get('clientes_cadastro', [])
            df = pd.json_normalize(clientes_list)
            return df
        else:
            print(f"Erro na requisição: {response.status_code} - {response.text}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# Chama o main
cont = 1  # Define a página como 2, conforme o exemplo
resultados = []

for i in range(100):
    print(f"Processando página {cont}...")
    df = main(cont)
    if not df.empty:
        resultados.append(df)
    cont += 1

if resultados:
    df_final = pd.concat(resultados, ignore_index=True)
    # Abre o arquivo em modo de apêndice, adicionando novas linhas ao final
    df_final.to_csv("CLIENTES/clientes.csv", mode='a', header=False, index=False)
    print("Novos dados foram adicionados ao arquivo 'clientes.csv'.")
else:
    print("Nenhum dado foi retornado.")
