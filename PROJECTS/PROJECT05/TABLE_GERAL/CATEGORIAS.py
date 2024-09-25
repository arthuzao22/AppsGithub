import requests
import pandas as pd
from tqdm import tqdm

def fetch_categories(page):
    url = "https://app.omie.com.br/api/v1/geral/categorias/"
    headers = {"Content-Type": "application/json"}
    
    body = {
        "call": "ListarCategorias",
        "app_key": "1102013231319",
        "app_secret": "2a332290a6173c88128adf1d7e31f4f9",
        "param": [{"pagina": page, "registros_por_pagina": 147}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=body, timeout=30, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        return None

def main():
    total_pages = 100  # Adjust this based on your API documentation
    results = []

    for page in tqdm(range(total_pages)):
        result = fetch_categories(page + 1)  # Start from page 2
        if not result:
            break
        
        categorias_list = result.get('categorias_list', [])
        if not categorias_list:
            print(f"Página {page + 1} não contém categorias. Parando a iteração.")
            break

        df = pd.json_normalize(categorias_list)
        results.append(df)

    if results:
        combined_df = pd.concat(results, ignore_index=True)
        combined_df.to_csv("categorias.csv", index=False)
        print(f"Todas as páginas foram processadas. Dados salvos em 'categorias.csv'.")
    else:
        print("Nenhum dado foi retornado.")

if __name__ == "__main__":
    main()
