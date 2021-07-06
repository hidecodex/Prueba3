from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.forms import UserCreationForm


# Paginas del menu.
def home (request):
    data = {}
    return render(request, 'home.html', data)
def mb (request):
    data = {}
    return render(request, 'mb.html', data)
def cpu (request):
    data = {}
    return render(request, 'cpu.html', data)
def gpu (request):
    data = {}
    return render(request, 'gpu.html', data)
def psu (request):
    data = {}
    return render(request, 'psu.html', data)
def ram (request):
    data = {}
    return render(request, 'ram.html', data)
def hdd (request):
    data = {}
    return render(request, 'hdd.html', data)
def ssd (request):
    data = {}
    return render(request, 'ssd.html', data)
def m2 (request):
    data = {}
    return render(request, 'm2.html', data)


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
