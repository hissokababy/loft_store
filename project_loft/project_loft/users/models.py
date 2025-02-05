from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='Город')
    street = models.CharField(max_length=150, blank=True, null=True, verbose_name='Улица')
    house_or_block = models.CharField(max_length=150, blank=True, null=True, verbose_name='Дом/Корпус')
    home_or_flat = models.CharField(max_length=150, blank=True, null=True, verbose_name='Квартира')
    
    
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
    

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    session_key = models.CharField(max_length=150, verbose_name='Сессия анонимного пользователя', blank=True, null=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя пользователя', blank=True, null=True)
    email = models.CharField(max_length=150, verbose_name='Почта пользователя', blank=True, null=True)
    message = models.TextField(verbose_name='Сообщение пользователя')
    
    
    def __str__(self):
        if self.user:
            return f'Заявка связи | Пользователь {self.user}'
        else:
            return f'Заявка связи | Пользователь анонимный'
    
    class Meta:
        verbose_name = 'Заявка на обратную связь'
        verbose_name_plural = 'Заявки на обратную связь'