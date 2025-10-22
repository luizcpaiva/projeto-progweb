from django.contrib import admin 
from .models import Categoria, Produto, Pedido, ItemPedido 
 
@admin.register(Categoria) 
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'slug') 
    prepopulated_fields = {'slug': ('nome',)} 
 
@admin.register(Produto) 
class ProdutoAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'disponivel') 
    list_filter = ('categoria', 'disponivel') 
    list_editable = ('preco', 'estoque', 'disponivel') 
 
class ItemPedidoInline(admin.TabularInline): 
    model = ItemPedido 
    raw_id_fields = ['produto'] 
    extra = 0 
 
@admin.register(Pedido) 
class PedidoAdmin(admin.ModelAdmin): 
    list_display = ('id', 'usuario', 'status', 'criado_em') 
    list_filter = ('status', 'criado_em') 
    inlines = [ItemPedidoInline]