from django.shortcuts import render, redirect, get_object_or_404
from app.forms import CarrosForm
from app.models import Carros
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

# Create
def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    data = {'form': form}  # Pass the form back in case of invalid data
    return render(request, 'form.html', data)

# View
def view(request, pk):
    data = {}
    data['db'] = get_object_or_404(Carros, pk=pk)  # Safely get object
    return render(request, 'view.html', data)

# Edit
def edit(request, pk):
    carro = get_object_or_404(Carros, pk=pk)  # Safely get object
    data = {}
    data['form'] = CarrosForm(instance=carro)
    return render(request, 'form.html', data)

# Update
def update(request, pk):
    carro = get_object_or_404(Carros, pk=pk)  # Safely get object
    form = CarrosForm(request.POST or None, instance=carro)
    if form.is_valid():
        form.save()  # Call save method with parentheses
        return redirect('home')
    data = {'form': form}  # Pass the form back in case of invalid data
    return render(request, 'form.html', data)


#delete
def delete(request, pk):
    carro = get_object_or_404(Carros, pk=pk)
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            auth_login(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('deu ruim')