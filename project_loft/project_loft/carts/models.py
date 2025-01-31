from django.db import models

from goods.models import Product
from users.models import User

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, name=True, verbose_name='Пользователь')
    session_key = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    
    def __str__(self):
        if self.user:
            return f'Корзина пользователя | {self.user.username}'
        else:
            return f'Корзина "Анонимного" пользователя'
    

    def products_price(self):
        return round(self.product.price - self.product.price*self.product.discount/100)


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        
        
    
    
    
    


