from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria
from django.contrib.auth import login
from .forms import RegisterForm
from django.db.models import Q

def index(request, category_slug=None):
    categoria_atual = None
    categorias = Categoria.objects.all()

    produtos = Produto.objects.filter(disponivel=True)

    query = request.GET.get('q')
    if query:
        produtos = produtos.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))

    if category_slug:
        categoria_atual = get_object_or_404(Categoria, slug=category_slug)
        produtos = produtos.filter(categoria=categoria_atual)

    context = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_atual': categoria_atual,
        'query': query # Envia o termo de busca de volta para o template
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