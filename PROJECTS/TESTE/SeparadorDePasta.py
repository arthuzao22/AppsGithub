import pandas as pd
import os
import PyPDF2

# Caminho do arquivo PDF
arquivo_pdf = r"d:\arquivos_movidos\AVL5_Teste_B_7°_ano_EF_II_2024_Matemática II_gabarito.pdf"

# Função para ler um PDF
def ler_pdf(arquivo_pdf):
    # Abre o arquivo PDF em modo leitura binária
    with open(arquivo_pdf, 'rb') as file:
        # Cria um objeto PDF Reader
        leitor = PyPDF2.PdfReader(file)
        
        # Tenta acessar a primeira página
        try:
            pagina = leitor.pages[0]  # A primeira página é a de índice 0
            texto = pagina.extract_text()  # Extrai o texto da primeira página
            return texto
        except IndexError:
            return "O PDF não contém páginas."

# Chama a função e imprime o resultado
texto_do_pdf = ler_pdf(arquivo_pdf)

# Exibe o texto extraído
print(f"Texto da primeira página:\n{texto_do_pdf}\n")
