from PyPDF2 import PdfReader, PdfWriter
import datetime
import os

# Função para gerar o nome do arquivo com base na data e hora
def gerar_nome_arquivo():
    agora = datetime.datetime.now()
    return agora.strftime('%Y-%m-%d_%H-%M-%S') + '.pdf'

# Função para separar as páginas de um PDF
def separar_paginas_pdf(caminho_arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return
    
    # Lê o PDF
    with open(caminho_arquivo, 'rb') as f:
        leitor_pdf = PdfReader(f)
        total_paginas = len(leitor_pdf.pages)
        
        # Para cada página do PDF, salva-a como um novo arquivo
        for numero_pagina in range(total_paginas):
            escritor_pdf = PdfWriter()
            pagina = leitor_pdf.pages[numero_pagina]
            escritor_pdf.add_page(pagina)
            
            # Salva a página como um novo arquivo PDF
            nome_pagina = f'pagina_{numero_pagina + 1}.pdf'
            with open(nome_pagina, 'wb') as nova_pagina:
                escritor_pdf.write(nova_pagina)
            
            print(f"Página {numero_pagina + 1} salva como {nome_pagina}")

# Exemplo de uso com um arquivo local
caminho_arquivo_pdf = r"c:\Users\João Pedro Cordeiro\Downloads\3A QUIMICA 2 BIM 2024.pdf"

# Separa as páginas do PDF
separar_paginas_pdf(caminho_arquivo_pdf)
