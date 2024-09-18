from PyPDF2 import PdfReader, PdfWriter
import os

# Função para limpar a pasta de destino
def limpar_pasta(pasta_destino):
    for item in os.listdir(pasta_destino):
        caminho_item = os.path.join(pasta_destino, item)
        if os.path.isfile(caminho_item):
            os.remove(caminho_item)


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
        
        # Define o diretório de destino
        pasta_destino = r"..\PROJECT03\PdfSeparado"
        
        # Cria o diretório se ele não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        else:
            # Limpa a pasta se ela já existir
            limpar_pasta(pasta_destino)
        
        # Para cada página do PDF, salva-a como um novo arquivo
        for numero_pagina in range(total_paginas):
            escritor_pdf = PdfWriter()
            pagina = leitor_pdf.pages[numero_pagina]
            escritor_pdf.add_page(pagina)
            
            # Define o nome e caminho do novo arquivo PDF
            nome_pagina = f'{numero_pagina + 1}.pdf'
            caminho_para_salvar_pdf = os.path.join(pasta_destino, nome_pagina)
            
            # Salva a página como um novo arquivo PDF
            with open(caminho_para_salvar_pdf, 'wb') as nova_pagina:
                escritor_pdf.write(nova_pagina)
            
            print(f"Página {numero_pagina + 1} salva como {caminho_para_salvar_pdf}")

# Exemplo de uso com um arquivo local
caminho_arquivo_pdf = r'c:\Users\João Pedro Cordeiro\Desktop\09- Adiantamento.pdf'

# Separa as páginas do PDF
separar_paginas_pdf(caminho_arquivo_pdf)
