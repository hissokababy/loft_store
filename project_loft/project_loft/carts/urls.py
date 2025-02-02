from django.urls import path

from carts.views import cart, cart_add, cart_delete

app_name = 'carts'

urlpatterns = [
    path('', cart, name='cart'),
    path('<slug:product_slug>/', cart_add, name='cart_add'),
    path('cart-delete/<slug:product_slug>/', cart_delete, name='cart_delete'),
    
]
