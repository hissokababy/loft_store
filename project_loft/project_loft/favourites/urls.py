from django.urls import path

from django.views.generic import TemplateView
from favourites.views import AddFavProductView

app_name = 'favourites'

urlpatterns = [
    path('', TemplateView.as_view(template_name='favourites/favourites.html'), name='favourites'),
    path('<slug:product_slug>/', AddFavProductView.as_view(), name='add_fav'),

]