from math import prod
from django.shortcuts import render

from goods.models import Category, Product
from home.utils import q_search

# Create your views here.


def catalog(request, category_slug=None):
    products = Product.objects.all()
    
    query = request.GET.get('q')
    
    if query:
        # products = q_search(query)   # надо подключить бд
        ...
        
    else:
        category = Category.objects.get(slug=category_slug)

        products = [
            i for i in products if (i.discount and category_slug == 'akciya')
            or i.category.parent == category 
            or category.slug == 'novinki'
            ]    
    
    context = {
        'products': products
        }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    
    
    context = {
        'product_main': product,
        'recommended_products': Product.objects.filter(category=product.category),
        'colors': Product.objects.filter(title=product.title),
        'product_main_quantity': [i for i in range(product.quantity)]
    }    
    
    
    return render(request, 'goods/product.html', context)
