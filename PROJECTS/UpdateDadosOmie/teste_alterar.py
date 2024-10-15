import requests
import pandas as pd
import certifi

def atualizar_movimento(movimento, key, secret):
    # Estrutura do corpo da requisição de atualização
    body = {
        "call": "AlterarContaPagar",  
        "app_key": key,
        "app_secret": secret,
        "param": [movimento]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://app.omie.com.br/api/v1/financas/contapagar/",
            headers=headers,
            json=body,
            timeout=60,
            verify=certifi.where()
        )

        # Verifique o status da resposta
        if response.status_code == 200:
            print(f"Movimento {movimento['codigo_lancamento_omie']} atualizado com sucesso.")
            print(response.json())  # Exibir a resposta completa da API
            return response.json()
        else:
            print(f"Erro na requisição: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro durante a requisição: {e}")



def carregar_dados_excel(caminho_excel):
    try:
        # Lê o Excel e retorna como DataFrame
        df = pd.read_excel(caminho_excel)
        print(f"Arquivo {caminho_excel} carregado com sucesso.")
        return df
    except FileNotFoundError:
        print("Arquivo Excel não encontrado.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao carregar o Excel: {e}")
        return pd.DataFrame()

# Configuração da integração
info = {
    'call': 'AlterarContaPagar',
    'app_key': '1102036231296',
    'app_secret': '9cf2dd9c9b2b1c714d3c9ee792f296ed'
}
key = info['app_key']
secret = info['app_secret']

# Caminho do Excel com os movimentos
caminho_excel = "Pasta1.xlsx"

# Carregar os dados do Excel
df_movimentos = carregar_dados_excel(caminho_excel)

# Verificar se há dados no DataFrame
if not df_movimentos.empty:
    # Iterar por cada linha do DataFrame e atualizar o movimento
    for index, row in df_movimentos.iterrows():
        movimento = {
            "codigo_lancamento_omie": row["codigo_lancamento_omie"],
            "codigo_cliente_fornecedor": row["codigo_cliente_fornecedor"],
            "data_vencimento": row["data_vencimento"],  # Converter para o formato dd/mm/aaaa
            "valor_documento": row["valor_documento"],
            "codigo_categoria": row["codigo_categoria"],
            "data_previsao": row["data_previsao"].strftime('%d/%m/%Y'),  # Converter para o formato dd/mm/aaaa
            "id_conta_corrente": row["id_conta_corrente"]
        }
        atualizar_movimento(movimento, key, secret)
else:
    print("Nenhum dado encontrado no Excel.")
