import requests
import pandas as pd
import os

empresa = input("INFORME A EMPRESA: ")

#####################################################################################################################################

data = {
    'Site': {'call': 'ListarCategorias', 'app_key': '1102005564660', 'app_secret': 'd58d70a49a3f5b3f536057d14c63fa4b'},  #36
    'Itamar': {'call': 'ListarCategorias', 'app_key': '1102013231319', 'app_secret': '2a332290a6173c88128adf1d7e31f4f9'},  #223
    'Gráfica Educa': {'call': 'ListarCategorias', 'app_key': '3165494501169', 'app_secret': '59919980813d7bd18f89104852eeade6'},  #10
    'CDG': {'call': 'ListarCategorias', 'app_key': '1102036231296', 'app_secret': '9cf2dd9c9b2b1c714d3c9ee792f296ed'},  #20
    'Benjamin': {'call': 'ListarCategorias', 'app_key': '1101921231411', 'app_secret': 'd69170e421eef351ca95ddd7fc390a5b'},  #200
    'CDF': {'call': 'ListarCategorias', 'app_key': '1271400395265', 'app_secret': '5bb6cf0aff2f6c167b8029494d6bf1d8'}  #10
}

info = data[empresa]
key = info['app_key']
secret = info['app_secret']

def main(cont):
    body = {
        "call": "ListarCategorias",
        "app_key": key,
        "app_secret": secret,
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
            "https://app.omie.com.br/api/v1/geral/categorias/",
            headers=headers,
            json=body,
            timeout=30,
            verify=False  # Desativa a verificação SSL
        )

        if response.status_code == 200:
            data = response.json()
            categorias_list = data.get('categorias', [])
            if categorias_list:
                df = pd.json_normalize(categorias_list)
                return df
            else:
                print("Nenhuma categoria retornado na página.")
                return pd.DataFrame()
        else:
            print(f"Erro na requisição: {response.status_code} - {response.text}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# Chama o main
cont = 1  # Define a página inicial
resultados = []

for i in range(10):
    print(f"Processando página {cont}...")
    df = main(cont)
    if not df.empty:
        resultados.append(df)
    else:
        print(f"Interrompendo o loop, sem dados na página {cont}.")
        break  # Se não houver dados, interrompe o loop
    cont += 1

if resultados:
    df_final = pd.concat(resultados, ignore_index=True)

    # Verifica se o arquivo já existe para decidir se escreve cabeçalho ou não
    output_file = f"CATEGORIAS/DADOS_CATEGORIAS/CATEGORIAS.csv"
    
    # Cria a pasta categorias se não existir
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Salva o DataFrame no arquivo CSV
    if os.path.exists(output_file):
        df_final.to_csv(output_file, mode='a', header=False, index=False)
        print("Novos dados foram adicionados ao arquivo 'categorias.csv'.")
    else:
        df_final.to_csv(output_file, header=True, index=False)
        print("Arquivo 'categorias.csv' criado com sucesso.")
else:
    print("Nenhum dado foi retornado.")
