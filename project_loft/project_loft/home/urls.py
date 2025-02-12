from django.urls import path
from home.views import IndexView, ContactView
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
