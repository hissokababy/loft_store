from django.urls import path

from orders.views import checkout, order_products_view

app_name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),    
    path('order_products/', order_products_view, name='order_products'),
]