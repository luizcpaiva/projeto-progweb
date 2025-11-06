from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_list'),
    path('register/', views.register, name='register'),
    path('categoria/<slug:category_slug>/', views.index, name='product_list_by_category'),
    path('add_to_cart/<int:produto_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrinho/', views.cart_detail, name='cart_detail'),
    path('carrinho/limpar/', views.clear_cart, name='clear_cart'),
    path('finalizar-compra/', views.checkout, name='checkout'),
    path('compra-sucesso/', views.checkout_success, name='checkout_success'),
]