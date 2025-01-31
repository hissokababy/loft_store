from django.urls import path

from carts.views import cart

app_name = 'carts'

urlpatterns = [
    path('', cart, name='cart')
    
]
