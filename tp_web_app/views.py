# myapp/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def index_na(request):
    return render(request, 'index_na.html')

def ask(request):
    return render(request, 'ask.html')