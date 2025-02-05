from django.shortcuts import render

from goods.models import Product
from users.models import Contact

# Create your views here.


def index(request):
    context = {
        'products' : Product.objects.all(),
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_message = request.POST.get('message')
        
        if request.user.is_authenticated:
            Contact.objects.create(
                user=request.user,
                first_name=contact_name,
                email=contact_email,
                message=contact_message,
            )       
        
        else:
            Contact.objects.create(
                first_name=contact_name,
                email=contact_email,
                message=contact_message,
            )  
    else:
        ...
    
    return render(request, 'home/contact.html')


