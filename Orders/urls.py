from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('orders', views.orders, name='orders'),
    path('search-order', views.search_order, name='search-order'),
    path('new-order', views.new_order, name='new-order'),
    path('edit-order/<int:id>', views.edit_order, name='edit-order'),
    path('print-order/<int:id>', views.print_order, name='print-order'),
    path('ordenes_csv', views.ordenes_csv, name='ordenes_csv'),
    path('shop/<int:id>', views.shop, name='shop')    
    
    ]