from django.urls import path
from home.views import index, about, contact 

app_name = 'home'

urlpatterns = [
    
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
