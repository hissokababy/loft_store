from math import prod
from django.shortcuts import render

from goods.models import Category, Product
from home.utils import q_search


from django.views.generic import ListView, DetailView
# Create your views here.


class CatalogView(ListView):
    model = Product
    template_name = 'goods/catalog.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # ПОЛНОТЕКСТОВЫЙ ПОИСК (ПОДКЛЮЧИТЬ НАДО ПОСТГРЕС)
        # query = self.request.GET.get('q')
    
        # if query:
        #     # products = q_search(query)   
        #     ...

        products = Product.objects.all()
        
        category = Category.objects.get(slug=self.kwargs['category_slug'])

        products = [
                    i for i in products if (i.discount and category.slug == 'akciya') 
                    or i.category.parent == category
                    or category.slug == 'novinki'
                    ]
        context['products'] = products
        context['category'] = category
        return context


class ProductView(DetailView):
    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    
    def get_object(self, queryset = None):
        product = Product.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        products = Product.objects.filter(title=product.title)
        context["product_main"] = product
        context['recommended_products'] = Product.objects.filter(category=product.category)
        context['colors'] = Product.objects.filter(title=product.title),
        context['product_main_quantity'] = [i for i in range(product.quantity)]
        print('[[[[[[[[[]]]]]]]]]')
        return context
    

# def product(request, product_slug):
#     product = Product.objects.get(slug=product_slug)
    
    
#     context = {
#         'product_main': product,
#         'recommended_products': Product.objects.filter(category=product.category),
#         'colors': Product.objects.filter(title=product.title),
#         'product_main_quantity': [i for i in range(product.quantity)]
#     }    
    
    
#     return render(request, 'goods/product.html', context)



# def catalog(request, category_slug=None):
#     products = Product.objects.all()
    
#     query = request.GET.get('q')
    
#     if query:
#         # products = q_search(query)   # надо подключить бд
#         ...
        
#     else:
#         category = Category.objects.get(slug=category_slug)

#         products = [
#             i for i in products if (i.discount and category_slug == 'akciya')
#             or i.category.parent == category 
#             or category.slug == 'novinki'
#             ]    
    
#     context = {
#         'products': products
#         }
#     return render(request, 'goods/catalog.html', context)