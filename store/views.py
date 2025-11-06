from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Pedido, ItemPedido
from django.contrib.auth import login
from .forms import RegisterForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='/contas/login/')
def add_to_cart(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.user.is_superuser:
        return HttpResponseForbidden("Administradores não podem adicionar itens ao carrinho.")

    pedido, criado = Pedido.objects.get_or_create(
        usuario=request.user,
        status='pendente'
    )

    item, item_criado = ItemPedido.objects.get_or_create(
        pedido=pedido,
        produto=produto,
        defaults={'preco': produto.preco} 
    )

    if not item_criado:
        item.quantidade += 1
        item.save()

    return redirect('product_list')

@login_required(login_url='/contas/login/')
def cart_detail(request):
    try:
        pedido = Pedido.objects.get(usuario=request.user, status='pendente')
        itens = ItemPedido.objects.filter(pedido=pedido)
    except Pedido.DoesNotExist:
        pedido = None
        itens = []

    context = {
        'pedido': pedido,
        'itens': itens
    }
    return render(request, 'cart/cart_detail.html', context)

@login_required(login_url='/contas/login/')
def clear_cart(request):
    try:
        pedido = Pedido.objects.get(usuario=request.user, status='pendente')

        pedido.delete()

    except Pedido.DoesNotExist:
        pass

    return redirect('cart_detail')

@login_required(login_url='/contas/login/')
def checkout(request):
    try:
        pedido = Pedido.objects.get(usuario=request.user, status='pendente')

        pedido.status = 'pago' 
        pedido.save()

        return redirect('checkout_success')

    except Pedido.DoesNotExist:
        return redirect('cart_detail')
    
def checkout_success(request):
    return render(request, 'cart/checkout_success.html')

@login_required(login_url='/contas/login/')
def order_history(request):
    pedidos = Pedido.objects.filter(
        usuario=request.user
    ).exclude(
        status='pendente'
    ).order_by('-criado_em') 

    context = {
        'pedidos': pedidos
    }
    return render(request, 'cart/order_history.html', context)