#-----------------------------------------------------------------------------------------------
#   CRIADOR: ARTHUR DOS REIS GONÇALVES
#   DATA: 12/09/2024
#   VERSÃO: 2.0
#   LINK DO APP: https://github.com/arthuzao22/AppsGithub/tree/main/PROJECTS/PROJECT02
#-----------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from pathlib import Path
import pandas as pd
from PyPDF2 import PdfReader
import datetime
import ttkthemes
import os

# Pega a data mais nova para ser utilizada no código
def data():
    agora = datetime.datetime.now()
    return agora.strftime('%Y-%m-%d_%H-%M-%S')

def ativar_informacoes():
    messagebox.showinfo("Como o App Funciona", 
                        "Este aplicativo tem as seguintes funcionalidades:\n\n"
                        "1. **Cadastro de Diretórios**: Insira o caminho da pasta para listar todos os arquivos PDF presentes.\n"
                        "2. **Análise de PDFs**: O aplicativo analisa cada arquivo PDF e conta o número de páginas.\n"
                        "3. **Geração de Relatórios**: Os resultados são salvos em um arquivo Excel na pasta 'Relatorios'.\n\n"
                        "Para usar o aplicativo:\n"
                        "1. Digite o caminho da pasta no campo de entrada.\n"
                        "2. Clique em 'Ativar' para processar a pasta.\n"
                        "3. O relatório será gerado e salvo na pasta 'Relatorios'.")
ativar_informacoes()

def SelecionarPasta():
    pasta_selecionada = filedialog.askdirectory()
    
    if pasta_selecionada:
        entrada.delete(0, tk.END)  # Limpa o campo de entrada
        entrada.insert(0, pasta_selecionada)  # Insere o caminho da pasta

def ativar_codigo():
    entrada_texto = entrada.get()  # Obtém o texto do campo de entrada
    messagebox.showinfo("Informação", f"URL ativada: {entrada_texto}")

    # Atualiza o caminho baseado no texto da entrada
    caminho = Path(entrada_texto)

    resultados = lista_pastas_e_arquivos(caminho)
    
    if isinstance(resultados, list):
        df_resultados = pd.DataFrame(resultados)
        
        # Obtém o diretório atual do script
        diretorio_atual = Path(os.path.dirname(os.path.abspath(__file__)))
        diretorio_relatorios = diretorio_atual / 'RELATORIOS'
        diretorio_relatorios.mkdir(parents=True, exist_ok=True)
        
        arquivo_excel = diretorio_relatorios / f'pastas_arquivos-{data()}.xlsx'
        
        # Apaga o arquivo se já existir
        if arquivo_excel.exists():
            arquivo_excel.unlink()
            print(f"Arquivo {arquivo_excel} existente foi apagado.")
        
        # Salva o DataFrame em um novo arquivo Excel
        df_resultados.to_excel(arquivo_excel, index=False)
        messagebox.showinfo("Arquivo salvo em: ", f"{arquivo_excel}")  
    else:
        resultado_label.config(text=f"Resultado: {resultados}")

def lista_pastas_e_arquivos(caminho):
    if caminho.exists():
        pastas_arquivos = []

        # Função recursiva para percorrer pastas e subpastas
        def percorrer_pastas(pasta):
            for item in pasta.iterdir():
                if item.is_dir():
                    percorrer_pastas(item)
                else:
                    if item.suffix.lower() == '.pdf':  # Verifica se o arquivo é PDF
                        try:
                            with open(item, 'rb') as file:
                                pdf = PdfReader(file)
                                quantidade_paginas = len(pdf.pages)  # Conta a qtde de paginas dentro 
                        except Exception as e:
                            quantidade_paginas = f'Erro: {e}'
                        
                        diretorio = item.parent  # Pega o diretório do arquivo
                        nome_pasta_antes_do_arquivo = diretorio.parent.name  # Antepenúltimo diretório
                        
                        pastas_arquivos.append({'Nome Pasta': nome_pasta_antes_do_arquivo, 'Nome': item.name, 'QTDE DE PAGINAS': quantidade_paginas, 'Caminho': str(item)})
                    else:
                        pastas_arquivos.append({'Nome': item.name, 'Caminho': str(item)})

        percorrer_pastas(caminho)

        if pastas_arquivos:
            return pastas_arquivos
        else:
            return "Nenhuma pasta ou arquivo encontrado no diretório."
    
    else:
        return f"O diretório {caminho} não foi encontrado."

#-----------------------------------------------------------------------------------------------
#---------------------------------------VIEWS LOGO ABAIXO---------------------------------------
#-----------------------------------------------------------------------------------------------

# Cria a janela principal
janela = tk.Tk()
janela.title("Relatório Qtde de páginas a serem impressas")

# Define o tamanho da janela
janela.geometry("350x200")  # Ajustado para acomodar todos os widgets

# Centraliza a janela na tela
janela.eval('tk::PlaceWindow . center')

# Cria um frame para centralizar os widgets
frame = tk.Frame(janela)
frame.pack(expand=True)

# Adiciona um título
titulo = tk.Label(frame, text="Digite a URL da pasta: ", font=("Arial", 12))
titulo.pack(pady=10)

# Cria um botão que chama a função SelecionarPasta quando pressionado
botao = tk.Button(frame, text="Selecionar Pasta", width=29, command=SelecionarPasta, bg="#4CAF50", fg="white", font=("Arial", 10))
botao.pack(pady=10)

# Cria um campo de entrada
entrada = tk.Entry(frame, width=40)
entrada.pack(pady=8)


# Cria um botão que chama a função ativar_codigo quando pressionado
botao = tk.Button(frame, text="Ativar", width=29, command=ativar_codigo, bg="#4CAF50", fg="white", font=("Arial", 10))
botao.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
