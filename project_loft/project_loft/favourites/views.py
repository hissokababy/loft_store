from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from goods.models import Product
from favourites.models import Favourite

# Create your views here.

class AddFavProductView(DetailView):
    template_name = 'favourites/favourites.html'
    slug_url_kwarg = 'product_slug'
    
    def get_object(self, queryset = None):
        product = Product.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        if not self.request.user.is_authenticated:
            fav_product, created = Favourite.objects.get_or_create(session_key=self.request.session.session_key, product=product)
        else:
            fav_product, created = Favourite.objects.get_or_create(user=self.request.user, product=product)
            
            
        if not created:
            messages.error(self.request, 'Товар удален из избранных')
            fav_product.delete()
        else:
            messages.success(self.request, 'Товар добавлен в избранное')

        referer = self.request.META.get('HTTP_REFERER', '/')    
        return redirect(referer)
    

# def add_fav_product(request, product_slug):
#     product = Product.objects.get(slug=product_slug)
    
#     if not request.user.is_authenticated:
#         fav_product, created = Favourite.objects.get_or_create(session_key=request.session.session_key, product=product)
#     else:
#         fav_product, created = Favourite.objects.get_or_create(user=request.user, product=product)
        
        
#     if not created:
#         messages.error(request, 'Товар удален из избранных')
#         fav_product.delete()
#     else:
#         messages.success(request, 'Товар добавлен в избранное')
        
        
        
#     referer = request.META.get('HTTP_REFERER', '/')    
        
#     return redirect(referer)



# def favourite(request):
#     return render(request, 'favourites/favourites.html')