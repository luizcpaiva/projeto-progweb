from .models import Pedido, ItemPedido

def cart_context(request):
    cart_item_count = 0
    if request.user.is_authenticated and not request.user.is_superuser:
        try:
            pedido = Pedido.objects.get(usuario=request.user, status='pendente')

            cart_item_count = ItemPedido.objects.filter(pedido=pedido).count()

        except Pedido.DoesNotExist:
            cart_item_count = 0

    return {
        'cart_item_count': cart_item_count
    }