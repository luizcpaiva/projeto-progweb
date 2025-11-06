from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria
from django.contrib.auth import login
from .forms import RegisterForm

def index(request, category_slug=None):
    categoria_atual = None
    if category_slug:
        categoria_atual = get_object_or_404(Categoria, slug=category_slug)

    categorias = Categoria.objects.all()

    if categoria_atual:
        produtos = Produto.objects.filter(categoria=categoria_atual, disponivel=True)
    else:
        produtos = Produto.objects.filter(disponivel=True)

    context = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_atual': categoria_atual
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})