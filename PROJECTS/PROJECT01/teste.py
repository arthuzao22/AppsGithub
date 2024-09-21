import requests
import pandas as pd

def main(cont):
    # Definir o corpo da requisição
    body = {
        "call": "ListarContasPagar",
        "app_key": "1102036231296",
        "app_secret": "9cf2dd9c9b2b1c714d3c9ee792f296ed",
        "param": [{
            "pagina": cont,  # Usar 'cont' aqui
            "registros_por_pagina": 100,
            "apenas_importado_api": "N"
        }]
    }

    # Definir cabeçalhos
    headers = {
        "Content-Type": "application/json"
    }

    # Fazer a requisição à API Omie
    response = requests.post(
        "https://app.omie.com.br/api/v1/financas/contapagar/",
        headers=headers,
        json=body
    )

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()

        # Extrair a lista de 'conta_pagar_cadastro'
        conta_pagar_cadastro = data.get('conta_pagar_cadastro', [])

        # Converter a lista em DataFrame
        df = pd.json_normalize(conta_pagar_cadastro)

        return df  # Retorna o DataFrame em vez de salvar diretamente
    else:
        print(f"Erro na requisição: {response.status_code}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# CHAMA O MAIN
cont = 1
resultados = []

for i in range(10):  # Correção do loop
    print(f"Processando página {cont}...")
    df = main(cont)
    if not df.empty:
        resultados.append(df)  # Adiciona os DataFrames à lista
    cont += 1

# Concatenar todos os DataFrames em um só
if resultados:
    df_final = pd.concat(resultados, ignore_index=True)
    df_final.to_excel("contas_pagar_omie.xlsx", index=False)
    print(resultados)
    print("Todos os dados foram salvos no arquivo 'contas_pagar_omie.xlsx'.")
else:
    print("Nenhum dado foi retornado.")
