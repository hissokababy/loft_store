from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    city = forms.CharField()
    delivery_address = forms.CharField()
    requires_delivery = forms.Select()
    payment_method = forms.Select()
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'city', 'delivery_address', 'requires_delivery', 
                'payment_method']
        

