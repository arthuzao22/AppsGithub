import tkinter as tk
from tkinter import messagebox, filedialog

class PDFAnalyzerView:
    def __init__(self, master):
        self.master = master
        self.master.title("Relatório Qtde de páginas a serem impressas")
        self.master.geometry("350x200")
        self.master.eval('tk::PlaceWindow . center')

        self.frame = tk.Frame(master)
        self.frame.pack(expand=True)

        self.titulo = tk.Label(self.frame, text="Digite a URL da pasta: ", font=("Arial", 12))
        self.titulo.pack(pady=10)

        self.botao_selecionar = tk.Button(self.frame, text="Selecionar Pasta", width=29, command=self.selecionar_pasta, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.botao_selecionar.pack(pady=10)

        self.entrada = tk.Entry(self.frame, width=40)
        self.entrada.pack(pady=8)

        self.botao_ativar = tk.Button(self.frame, text="Ativar", width=29, command=None, bg="#4CAF50", fg="white", font=("Arial", 10))
        self.botao_ativar.pack(pady=10)

        self.controller = None

    def selecionar_pasta(self):
        pasta_selecionada = filedialog.askdirectory()
        if pasta_selecionada:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, pasta_selecionada)

    def set_controller(self, controller):
        self.controller = controller
        self.botao_ativar.config(command=self.controller.ativar_codigo)

    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
