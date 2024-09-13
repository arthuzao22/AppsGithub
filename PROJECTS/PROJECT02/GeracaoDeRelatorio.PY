import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import PhotoImage
import pandas as pd
import os
from PyPDF2 import PdfReader 
import datetime

# Pega a data mais nova para ser utilizada no código
def data():
    agora = datetime.datetime.now()
    return agora.strftime('%Y-%m-%d_%H-%M-%S')

def ativar_codigo():
    entrada_texto = entrada.get()  # Obtém o texto do campo de entrada
    messagebox.showinfo("Informação", f"URL ativada: {entrada_texto}")

    # Atualiza o caminho baseado no texto da entrada
    caminho = Path(entrada_texto)

    resultados = lista_pastas_e_arquivos(caminho)
    
    if isinstance(resultados, list):
        df_resultados = pd.DataFrame(resultados)
        
        diretorio_relatorios = Path('Relatorios')
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

#--------------------------------------------------------------------------------------------
#-------------------------------CRIAÇÃO DO FRONT-END DO APP----------------------------------
#--------------------------------------------------------------------------------------------
# Função de exemplo a ser chamada pelo botão
def ativar_codigo():
    messagebox.showinfo("Informação", f"Informe uma Url no campo")


# Cria a janela principal
janela = tk.Tk()
janela.title("Relatório Qtde de páginas a serem impressas")

# Define o tamanho da janela
janela.geometry("350x170")  # Largura x Altura

# Centraliza a janela na tela
janela.eval('tk::PlaceWindow . center')

# Cria um frame para centralizar os widgets
frame = tk.Frame(janela)
frame.pack(expand=True)

# Adiciona um título
titulo = tk.Label(frame, text="Digite a URL da pasta: ", font=("Arial", 12))
titulo.pack(pady=10)

# Cria um campo de entrada
entrada = tk.Entry(frame, width=40)
entrada.pack(pady=8)

# Cria um botão que chama a função ativar_codigo quando pressionado
botao = tk.Button(frame, text="Ativar", width=29, command=ativar_codigo, bg="#4CAF50", fg="white", font=("Arial", 10))
botao.pack(pady=10)

# Cria um botão que chama a função ativar_codigo quando pressionado
botao = tk.Button(frame, text="Ativar", width=29, command=ativar_codigo, fg="white", font=("Arial", 10))
botao.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
