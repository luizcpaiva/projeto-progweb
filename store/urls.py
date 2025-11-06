from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product_list'),
    path('register/', views.register, name='register'),
    path('categoria/<slug:category_slug>/', views.index, name='product_list_by_category'),
]