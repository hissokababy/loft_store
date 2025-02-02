from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from goods.models import Product
from favourites.models import Favourite

# Create your views here.


def favourite(request):
    return render(request, 'favourites/favourites.html')


def add_fav_product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    
    if not request.user.is_authenticated:
        fav_product, created = Favourite.objects.get_or_create(session_key=request.session.session_key, product=product)
    else:
        fav_product, created = Favourite.objects.get_or_create(user=request.user, product=product)
        
        
    if not created:
        messages.error(request, 'Товар удален из избранных')
        fav_product.delete()
    else:
        messages.success(request, 'Товар добавлен в избранное')
        
        
        
    referer = request.META.get('HTTP_REFERER', '/')    
        
    return redirect(referer)

