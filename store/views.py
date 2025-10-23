from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'index.html', {'produtos': produtos})