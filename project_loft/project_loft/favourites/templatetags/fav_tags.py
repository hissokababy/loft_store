

from django import template

from favourites.models import Favourite


register = template.Library()


@register.simple_tag()
def get_fav_products(request):
    if request.user.is_authenticated:
        products = Favourite.objects.filter(user=request.user)
        return [i.product for i in products]
    
    if not request.session.session_key:
        request.session.create()
    products = Favourite.objects.filter(session_key=request.session.session_key)
    return [i.product for i in products]

