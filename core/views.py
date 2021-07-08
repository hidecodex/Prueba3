from core.models import Componente, Producto
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm



# Paginas del menu.
def home (request):
    Productos = Producto.objects.all()
    data = {"Productos":Productos}
    return render(request, 'home.html', data)

def mb (request):
    componente = Componente.objects.get(Nombre='mb')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'mb.html', data)
def cpu (request):
    componente = Componente.objects.get(Nombre='cpu')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'cpu.html', data)
def gpu (request):
    componente = Componente.objects.get(Nombre='gpu')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'gpu.html', data)
def psu (request):
    componente = Componente.objects.get(Nombre='psu')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'psu.html', data)
def ram (request):
    componente = Componente.objects.get(Nombre='ram')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'ram.html', data)
def hdd (request):
    componente = Componente.objects.get(Nombre='hdd')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'hdd.html', data)
def ssd (request):
    componente = Componente.objects.get(Nombre='ssd')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'ssd.html', data)
def m2 (request):
    componente = Componente.objects.get(Nombre='m2')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'm2.html', data)
    
def admin (request):
    Productos = Producto.objects.all()
    data = {"Productos":Productos}
    return render(request, 'admin.html', data)

def SignIn(request):
    contexto = {}
    return render(request, 'signin.html', contexto)
def registro(request):
    contexto = {}
    return render(request, 'registro.html', contexto)
def Logeando(request):
    username = request.POST.get('usuario','')
    password = request.POST.get('clave', '')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('index')
    else:
        return redirect('SignIn')
def Deslogeo(request):
    logout(request)
    return redirect('index')

