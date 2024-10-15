from django import forms  # Importa o módulo forms corretamente
from django.forms import ModelForm
from app.models import Funcionarios, Login

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = [
            'nome', 
            'registro', 
            'funcao', 
            'data_nascimento', 
            'data_admissao', 
            'cpf', 
            'conta_inter', 
            'ultimo_exame', 
            'proximo_exame', 
            'email', 
            'salario'
        ]

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = [
            'username',
            'password'
        ]
