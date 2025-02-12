from django.shortcuts import redirect, render
from django.contrib import messages
from goods.models import Product
from carts.models import Cart
from django.views.generic import View

# Create your views here.

class CartView(View):
    template_name = 'carts/cart.html'
    
    def get(self, request):
        return redirect('carts:cart')
    
    def post(self, request):
        try:
            product_slug = request.POST.get('product')
            product = Product.objects.get(slug=product_slug)
            print(f'слаг из запроса {product_slug}, {product.slug} товар их бд по запросу (его слаг)')
            action = request.POST.get('action')
                        
            if product_slug:
                if request.user.is_authenticated:
                    cart_product = Cart.objects.get(product__slug=product_slug, user=request.user)
                else:
                    cart_product = Cart.objects.get(product__slug=product_slug, session_key=request.session.session_key)

                if cart_product.quantity > 1 and action == 'dec':
                    cart_product.quantity -= 1
                    cart_product.save()
                    
                elif action == 'dec' and cart_product.quantity <= 1:
                    cart_product.delete()
                
                elif cart_product.quantity >= 1 and action == 'inc' and cart_product.quantity < product.quantity:
                    cart_product.quantity += 1
                    if cart_product.quantity > product.quantity:
                        cart_product.quantity = product.quantity
                    cart_product.save()
                
                return redirect('carts:cart')                
        except Exception as e:
            print(f'Ошибка: {e}')
        
        return redirect('carts:cart')


# def cart(request):

#     if not request.user.is_authenticated:    
#         cart_products = Cart.objects.filter(session_key=request.session.session_key)
            
#     else:
#         cart_products = Cart.objects.filter(user=request.user)

    
#     try:
#         product_slug = request.POST.get('product')
#         product = Product.objects.get(slug=product_slug)
#         print(f'слаг из запроса {product_slug}, {product.slug} товар их бд по запросу (его слаг)')
#         action = request.POST.get('action')
                    
#         if product_slug:
#             if request.user.is_authenticated:
#                 cart_product = Cart.objects.get(product__slug=product_slug, user=request.user)
#             else:
#                 cart_product = Cart.objects.get(product__slug=product_slug, session_key=request.session.session_key)

#             if cart_product.quantity > 1 and action == 'dec':
#                 cart_product.quantity -= 1
#                 cart_product.save()
                
#             elif action == 'dec' and cart_product.quantity <= 1:
#                 cart_product.delete()
            
#             elif cart_product.quantity >= 1 and action == 'inc' and cart_product.quantity < product.quantity:
#                 cart_product.quantity += 1
#                 if cart_product.quantity > product.quantity:
#                     cart_product.quantity = product.quantity
#                 cart_product.save()
            
#             return redirect('carts:cart')                
#     except Exception as e:
#         print(f'Ошибка: {e}')
    
#     context = {
#         'cart_products': cart_products,
#         'products': Product.objects.all()
#     }
    
#     return render(request, 'carts/cart.html', context)


def cart_add(request, product_slug):
    if not request.user.is_authenticated:
        product = Product.objects.get(slug=product_slug)
        cart_product, created = Cart.objects.update_or_create(product=product, session_key=request.session.session_key)
    
    else:
        if request.user.is_authenticated:
            product = Product.objects.get(slug=product_slug)
            cart_product, created = Cart.objects.update_or_create(product=product, user=request.user)
        
    
    num = request.GET.get('quantity')
        
    if not created:
        if cart_product.quantity < product.quantity:
            if num:
                cart_product.quantity += int(num)
            else:
                cart_product.quantity += 1
                    
            cart_product.save()
            messages.success(request, 'Товар добавлен в корзину')
    else:
        if num:
            cart_product.quantity += int(num)
        else:
            cart_product.quantity += 1
                
        cart_product.save()
        messages.success(request, 'Товар добавлен в корзину')
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

            
        
def cart_delete(request, product_slug):
    if not request.user.is_authenticated:
        cart_product = Cart.objects.get(session_key=request.session.session_key, product__slug=product_slug)
        cart_products = Cart.objects.filter(session_key=request.session.session_key)

    else:
        cart_product = Cart.objects.get(user=request.user, product__slug=product_slug)
        cart_products = Cart.objects.filter(user=request.user)

    cart_product.delete()
    

    [i.delete() for i in cart_products if i.quantity > 1]
    
    messages.warning(request, 'Товар удален из корзины')
    
    return redirect('carts:cart')

        
    
    
    