from django.urls import path

from favourites.views import favourite, add_fav_product

app_name = 'favourites'

urlpatterns = [
    path('', favourite, name='favourites'),
    path('<slug:product_slug>/', add_fav_product, name='add_fav'),

]