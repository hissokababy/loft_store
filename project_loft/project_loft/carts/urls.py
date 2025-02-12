from django.urls import path

from carts.views import CartView, cart_add, cart_delete

app_name = 'carts'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('<slug:product_slug>/', cart_add, name='cart_add'),
    path('cart-delete/<slug:product_slug>/', cart_delete, name='cart_delete'),
    
]
