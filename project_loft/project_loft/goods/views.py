from math import prod
from django.shortcuts import render

from goods.models import Category, Product

# Create your views here.


def catalog(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.all()
    
    products = [
        i for i in products if (i.discount and category_slug == 'akciya')
        or i.category.parent == category 
        or category.slug == 'novinki'
        ]
    
    context = {
        'category': category,
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
    musor = ['Длина', 'Ширина', 'Высота']
    lst = ' '.join([i for i in product.size.split(' ') if i not in musor])
    
    x = ''.join(lst.split())
    
    print(''.join(x.split('х')).replace('см', ' СМ '))
    
    
    
    return render(request, 'goods/product.html', context)
