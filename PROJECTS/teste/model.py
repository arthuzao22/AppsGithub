import pandas as pd
import os

CSV_FILE = 'usuarios.csv'

class UserModel:
    def __init__(self):
        if not os.path.exists(CSV_FILE):
            df = pd.DataFrame(columns=['ID', 'Nome', 'Email', 'cpf'])
            df.to_csv(CSV_FILE, index=False)

    def add_user(self, nome, email, cpf):
        df = pd.read_csv(CSV_FILE)
        new_id = df['ID'].max() + 1 if not df.empty else 1
        new_user = pd.DataFrame({'ID': [new_id], 'Nome': [nome], 'Email': [email], 'cpf': [cpf]})
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)

    def get_users(self):
        return pd.read_csv(CSV_FILE)

    def update_user(self, user_id, new_nome=None, new_email=None):
        df = pd.read_csv(CSV_FILE)
        if user_id in df['ID'].values:
            if new_nome:
                df.loc[df['ID'] == user_id, 'Nome'] = new_nome
            if new_email:
                df.loc[df['ID'] == user_id, 'Email'] = new_email
            if new_cpf:
                df.loc[df['ID'] == user_id, 'cpf'] = new_cpf
            df.to_csv(CSV_FILE, index=False)

    def remove_user(self, user_id):
        df = pd.read_csv(CSV_FILE)
        df = df[df['ID'] != user_id]
        df.to_csv(CSV_FILE, index=False)
