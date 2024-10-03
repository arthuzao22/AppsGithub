import pandas as pd
from sqlalchemy import create_engine, text

# Função para criar a engine de conexão com o banco de dados
def criar_conexao():
    conn_str = (
        "mssql+pyodbc:///?odbc_connect="
        "DRIVER={ODBC Driver 17 for SQL Server};" 
        "SERVER=DESKTOP-2MF5QCV;"  # Seu servidor
        "DATABASE=BASE_LISTAR_MOVIMENTOS;"  # Seu banco de dados
        "Trusted_Connection=yes;"  # Conexão autenticada
    )
    return create_engine(conn_str)

# Função para executar uma query SQL (DELETE, UPDATE, etc.)
def executar_query(engine, query):
    try:
        with engine.begin() as connection:  # Usando transaction.begin() para commit automático
            connection.execute(text(query))
            print("Query executada com sucesso.")
    except Exception as e:
        print(f"Erro ao executar a query: {e}")

# Função para carregar dados do CSV para um DataFrame
def carregar_csv(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv)
        print("Arquivo CSV carregado com sucesso.")
        print("Tipos de dados do DataFrame:")
        print(df.dtypes)
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo CSV: {e}")
        return None

# Função para inserir os dados do DataFrame no banco de dados
def inserir_dados(engine, df, table_name, if_exists='append'):
    try:
        df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
        print(f"Dados inseridos com sucesso na tabela {table_name}!")
    except Exception as e:
        print(f"Erro ao inserir dados na tabela {table_name}: {e}")

# Função principal para executar as operações de deletar e inserir dados
def processar_dados():
    # Criando a engine de conexão
    engine = criar_conexao()

    # Query de DELETE
    query_delete = """
        SELECT * FROM [CONTAS_GERAL_GRAFICA_EDUCA]
    """

    # Executando a query de DELETE
    executar_query(engine, query_delete)

    # Caminho do arquivo CSV
    csv_file = r'..\PROJECT05\Dados\contas_GERAL_omie_EDUCA.csv'
    
    # Nome da tabela no SQL Server
    table_name = 'CONTAS_GERAL_GRAFICA_EDUCA'

    # Carregando o CSV
    df = carregar_csv(csv_file)
    
    if df is not None:
        # Criando uma tabela temporária para testar
        inserir_dados(engine, df.head(10), 'TempTable', if_exists='replace')

        # Inserindo os dados na tabela principal
        inserir_dados(engine, df, table_name, if_exists='append')

# Executa o processo
processar_dados()
