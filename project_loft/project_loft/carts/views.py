from django.shortcuts import redirect, render
from django.contrib import messages
from goods.models import Product
from carts.models import Cart

# Create your views here.

def cart(request):
    
    if not request.user.is_authenticated:    
        cart_products = Cart.objects.filter(session_key=request.session.session_key)
    else:
        cart_products = Cart.objects.filter(user=request.user)
    
    context = {
        'cart_products': cart_products,
        'products': Product.objects.all()
    }
                
    return render(request, 'carts/cart.html', context)


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
    

    [i.delete() for i in cart_products if i.quantity == 0]
    
    messages.warning(request, 'Товар удален из корзины')
    
    return redirect('carts:cart')

        
    
    
    