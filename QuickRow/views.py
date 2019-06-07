from django.shortcuts import render


def index(request):
    return render(request, 'QuickRow/aluno/index.html', {})
