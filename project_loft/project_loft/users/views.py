from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from users.forms import LoginForm, ProfileForm, RegisterForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/registration.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Успешный вход в аккаунт')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Неверный логин или пароль')
        return super().form_invalid(form)


class UserRegistrerView(CreateView):
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        user = form.instance
        if user:
            form.save()
            auth.login(self.request, user)
            messages.success(self.request, 'Регистрация прошла успешно')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Неверный формат данных')
        return super().form_invalid(form)
    
class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')
    
    def get_object(self, queryset = None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Личные данные изменены')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Неверный формат данных')
        return super().form_invalid(form)
    
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.error(request, 'Вы вышли с аккаунта')
    return redirect(request.META.get('HTTP_REFERER', '/'))

# def profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ProfileForm(data=request.POST, instance=request.user)
#             if form.is_valid:
#                 form.save()
#                 messages.success(request, 'Личные данные изменены')
                
#             else:
#                 messages.error(request, 'Неверный формат данных')
#                 return redirect ('users:profile')
            
#         else:
#             form = ProfileForm(instance=request.user)

#     else:
#         form = ProfileForm()
        
        
#     context = {
#         'form': form,
#     }
    
#     return render(request, 'users/profile.html', context)


# def register(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#                 form = RegisterForm(data=request.POST)
#                 if form.is_valid():
#                     form.save()
#                     user = form.instance
#                     auth.login(request, user)
#                     messages.success(request, 'Регистрация прошла успешно')
#                     return redirect('home:index')
                
#                 else:
#                     messages.error(request, 'Неверный формат данных')
#         else:
#             form = RegisterForm()
            
#         context = {
#             'register_form': form
#         }
            
#         return render(request, 'users/registration.html', context)
#     else:
#         return redirect(request.META.get('HTTP_REFERER', '/'))
        
# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#                 form = LoginForm(data=request.POST)
#                 if form.is_valid():
#                     username = request.POST['username']
#                     password = request.POST['password']
#                     user = auth.authenticate(username=username, password=password)
#                     if user:
#                         auth.login(request, user)
#                         messages.success(request, 'Успешный вход в аккаунт')
#                         return redirect('home:index')
#                 else:
#                     messages.error(request, 'Неверный логин или пароль')
#         else:
#             form = LoginForm()
            
#         context = {
#             'login_form': form
#         }
#         return render(request, 'users/registration.html', context)
#     else:
#         return redirect(request.META.get('HTTP_REFERER', '/'))