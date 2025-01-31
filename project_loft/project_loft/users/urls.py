from django.urls import path

from users.views import login_view, logout, register, profile

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile')
]
