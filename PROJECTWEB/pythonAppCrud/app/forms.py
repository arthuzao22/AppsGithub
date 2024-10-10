from django.forms import ModelForm
from app.models import Funcionarios

class FuncionariosForm(ModelForm):
    
    class Meta:
        model = Funcionarios
        fields = ['nome', 'registro', 'funcao', 'data_nascimento', 'data_admissao', 'cpf', 'conta_inter', 'ultimo_exame', 'proximo_exame', 'email', 'salario']
