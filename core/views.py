from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login as auth_login

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

    data = {}
    return render(request, 'registro.html', data)

    logout(request)
    return redirect('Inicio')
    