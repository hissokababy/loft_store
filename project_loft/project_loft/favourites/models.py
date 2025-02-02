from django.db import models
from users.models import User

from goods.models import Product

# Create your models here.


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь', related_name='favourites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        if self.user:
            return f'Избранное пользователя | {self.user.username}'
        else:
            return f'Избранное "Анонимного" пользователя'
    
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
    
    
    
    
    