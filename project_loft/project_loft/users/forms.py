from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class LoginForm(AuthenticationForm):
    
    username = forms.CharField()
    password = forms.PasswordInput()
    
    class Meta:
        model = User
        fields = ['username', 'password']    
    

class RegisterForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'phone_number','password1', 'password2']    



class ProfileForm(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)
    house_or_block = forms.CharField(required=False)
    home_or_flat = forms.CharField(required=False)
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'street', 'house_or_block', 'home_or_flat']    


