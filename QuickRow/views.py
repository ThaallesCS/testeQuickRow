from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, 'QuickRow/aluno/index.html', {})


def select_senha(request):
    return render(request, 'QuickRow/aluno/selectSenha.html', {})
