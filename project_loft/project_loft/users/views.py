from django.contrib import auth, messages
from django.shortcuts import redirect, render

from users.forms import LoginForm, ProfileForm, RegisterForm

# Create your views here.

def login_view(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = LoginForm(data=request.POST)
                if form.is_valid():
                    username = request.POST['username']
                    password = request.POST['password']
                    user = auth.authenticate(username=username, password=password)
                    if user:
                        auth.login(request, user)
                        messages.success(request, 'Успешный вход в аккаунт')
                        return redirect('home:index')
                
                else:
                    messages.error(request, 'Неверный логин или пароль')
        else:
            form = LoginForm()
                
        context = {
            'login_form': form
        }
        return render(request, 'users/registration.html', context)
          
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = RegisterForm(data=request.POST)
                if form.is_valid():
                    form.save()
                    user = form.instance
                    auth.login(request, user)
                    messages.success(request, 'Регистрация прошла успешно')
                    return redirect('home:index')
                
                else:
                    messages.error(request, 'Неверный формат данных')
                
        else:
            form = RegisterForm()
            
        context = {
            'register_form': form
        }
            
        return render(request, 'users/registration.html', context)

    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.error(request, 'Вы вышли с аккаунта')
    return redirect(request.META.get('HTTP_REFERER', '/'))



def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(data=request.POST, instance=request.user)
            if form.is_valid:
                form.save()
                messages.success(request, 'Личные данные изменены')
                
            else:
                messages.error(request, 'Неверный формат данных')
                return redirect ('users:profile')
            
        else:
            form = ProfileForm(instance=request.user)
        
    else:
        form = ProfileForm()
        
    user_orders = request.user.orders.all()
        
    order_products = [i.order_products.all() for i in user_orders]
    context = {
        'form': form,
        # 'user_order_products': order_products,
        # 'user_orders': user_orders
    }
    
    return render(request, 'users/profile.html', context)