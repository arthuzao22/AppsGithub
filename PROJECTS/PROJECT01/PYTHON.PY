import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# Definir a string de conexão
conn_string = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-2MF5QCV;'
    r'Trusted_Connection=yes;'
)

# Criar uma engine de conexão usando SQLAlchemy
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_string}")

# Ler o arquivo Excel
excel_file = 'Área de Trabalho\Contas_a_Pagar_11092024.xlsx'
df = pd.read_excel(excel_file)

# Inserir os dados no banco de dados
df.to_sql('NomeDaTabela', con=engine, schema='dbo', if_exists='replace', index=False)

print("Dados importados com sucesso!")
