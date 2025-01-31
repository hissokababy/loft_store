from django import template

from goods.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=None)


@register.simple_tag()
def get_normal_price(sell_price):
    return f"{int(sell_price):_}".replace("_", " ")

@register.simple_tag()
def get_normal_size(product_size):
    musor = ['Длина', 'Ширина', 'Высота']
    lst = ' '.join([i for i in product_size.split(' ') if i not in musor])
    
    return lst


@register.simple_tag()
def get_card_size(product_size):
    lst =get_normal_size(product_size)
    x = ''.join(lst.split())
    
    msg = (' '.join(x.split('х')).replace('см', ' ').split())
    
    return msg
    

    