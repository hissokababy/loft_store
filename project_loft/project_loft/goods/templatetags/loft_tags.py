from django import template
from django.utils.http import urlencode
from goods.models import Category, Product
from carts.models import Cart

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=None)

@register.simple_tag()
def get_products():
    return Product.objects.all()


@register.simple_tag()
def get_normal_price(sell_price):
    return f"{int(sell_price):_}".replace("_", " ")

@register.simple_tag()
def get_normal_size(product_size):
    musor = ['Длина', 'Ширина', 'Высота']
    lst = ' '.join([i for i in product_size.split(' ') if i not in musor])
    
    return lst.replace('см', 'СМ')


@register.simple_tag()
def get_card_size(product_size):
    lst = get_normal_size(product_size).replace(' СМ', '').replace(' х ', ' ').split(' ')

    return lst
    

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()



@register.simple_tag()
def get_user_cart_products(request):
    if request.user.is_authenticated:
        carts =  request.user.carts.all()
        return [i.product for i in carts]
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key)
        return [i.product for i in carts]

