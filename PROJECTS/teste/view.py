import tkinter as tk
from tkinter import ttk, messagebox

class UserView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Cadastro de Usuários")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Centralizar a janela
        self.centralizar_janela()

        # Criar frame para formulário
        self.frame_form = tk.Frame(root)
        self.frame_form.pack(padx=10, pady=10)

        # Colocar os campos lado a lado
        tk.Label(self.frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame_form, width=20)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_form, text="Email:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_form, width=20)
        self.entry_email.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_form, text="CPF:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.frame_form, width=20)
        self.entry_cpf.grid(row=0, column=5, padx=5, pady=5)

        # Botões
        self.btn_add = tk.Button(self.frame_form, text="Adicionar", command=self.adicionar_usuario)
        self.btn_add.grid(row=2, column=0, pady=10)

        self.btn_update = tk.Button(self.frame_form, text="Atualizar", command=self.atualizar_usuario)
        self.btn_update.grid(row=2, column=1, pady=10)

        # Tabela de usuários (Treeview)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Email", "cpf"), show="headings", height=8)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("cpf", text="cpf")

        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("cpf", width=200)

        self.tree.pack(pady=20)

        # Botão de Remover
        self.btn_remove = tk.Button(self.root, text="Remover", command=self.remover_usuario)
        self.btn_remove.pack(pady=10)

        self.atualizar_lista()

    def centralizar_janela(self):
        largura = 600
        altura = 400
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        pos_x = (largura_tela // 2) - (largura // 2)
        pos_y = (altura_tela // 2) - (altura // 2)
        self.root.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

    def adicionar_usuario(self):
        nome = self.entry_name.get()
        email = self.entry_email.get()
        cpf = self.entry_cpf.get()
        if nome and email:
            self.controller.add_user(nome, email, cpf)
            self.atualizar_lista()
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def atualizar_usuario(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = self.tree.item(selected_item)['values'][0]
            new_nome = self.entry_name.get()
            new_email = self.entry_email.get()
            new_cpf = self.entry_cpf.get()
            self.controller.update_user(user_id, new_nome, new_email, new_cpf)
            self.atualizar_lista()
        else:
            messagebox.showwarning("Erro", "Selecione um usuário para atualizar.")

    def remover_usuario(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = self.tree.item(selected_item)['values'][0]
            self.controller.remove_user(user_id)
            self.atualizar_lista()
        else:
            messagebox.showwarning("Erro", "Selecione um usuário para remover.")

    def atualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        users = self.controller.get_users()
        for _, row in users.iterrows():
            self.tree.insert("", tk.END, values=(row["ID"], row["Nome"], row["Email"], row["cpf"]))
