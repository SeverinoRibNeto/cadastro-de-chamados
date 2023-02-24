from django.shortcuts import render


def cadastro_usuario(request):
    return render(request, "Cadastro")


def login_usuario(request):
    return render(request, 'login.html')
