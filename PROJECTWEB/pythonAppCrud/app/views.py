from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password, check_password  # Correção dos nomes das funções
from app.forms import FuncionariosForm, LoginForm
from app.models import Login, Funcionarios

# Create your views here.
def home(request):
    data = {'db': Funcionarios.objects.all()}
    return render(request, 'index.html', data)

def form(request):
    data = {'form': FuncionariosForm()}
    return render(request, 'Funcionarios/form.html', data)

# Create
def create(request):
    form = FuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Funcionário criado com sucesso!")
        return redirect('indexFuncionarios')
    data = {'form': form}
    return render(request, 'Funcionarios/form.html', data)

# View
def view(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    return render(request, 'Funcionarios/view.html', {'db': funcionario})

# Edit
def edit(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    form = FuncionariosForm(instance=funcionario)
    return render(request, 'Funcionarios/form.html', {'form': form, 'db': funcionario})

# Update
def update(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    form = FuncionariosForm(request.POST, instance=funcionario)
    if form.is_valid():
        form.save()
        messages.success(request, "Funcionário atualizado com sucesso!")
        return redirect('indexFuncionarios')
    return render(request, 'Funcionarios/form.html', {'form': form, 'db': funcionario})

# Index Funcionarios
def indexFuncionarios(request):
    data = {'db': Funcionarios.objects.all()}
    return render(request, 'Funcionarios/indexFuncionarios.html', data)

# Delete
def delete(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    funcionario.delete()
    messages.success(request, "Funcionário deletado com sucesso!")
    return redirect('indexFuncionarios')

# Login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Verificar se os campos estão preenchidos
        if not all([username, password]):
            messages.error(request, "Por favor, insira um nome de usuário e senha.")
            return render(request, 'login/login.html')
        
        # Tentar autenticar o usuário
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login bem-sucedido!")
            return redirect('indexFuncionarios')
        else:
            messages.error(request, "Credenciais inválidas")
    
    return render(request, 'login/login.html')
