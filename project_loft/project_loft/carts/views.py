from django.shortcuts import render

from goods.models import Product

# Create your views here.

def cart(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'carts/cart.html', context)

