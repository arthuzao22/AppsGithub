from model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def add_user(self, nome, email, cpf):
        self.model.add_user(nome, email, cpf)

    def get_users(self):
        return self.model.get_users()

    def update_user(self, user_id, new_nome=None, new_email=None, new_cpf=None):
        self.model.update_user(user_id, new_nome, new_email, new_cpf)

    def remove_user(self, user_id):
        self.model.remove_user(user_id)
