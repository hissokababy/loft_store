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
    
    