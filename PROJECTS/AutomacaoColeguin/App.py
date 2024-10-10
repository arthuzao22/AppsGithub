import pandas as pd

# Caminho para o arquivo Excel
urlPasta = r'C:\Users\João Pedro Cordeiro\Downloads\Pedido - P4 + Projeto Familia (2).xlsx'
arquivo_excel = pd.ExcelFile(urlPasta)
nomes_abas = arquivo_excel.sheet_names

# Exibir os nomes das abas
print("Nomes das abas:", nomes_abas)

# Ler a segunda aba (lembre-se que o índice é 0, então sheet_name=1 é a segunda aba)
segunda_pagina = pd.read_excel(urlPasta, sheet_name=1)

# Exibir os dados da segunda aba
print(segunda_pagina)
