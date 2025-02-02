from django.db import models

from goods.models import Product
from users.models import User

# Create your models here.

class CartQuery(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price for cart in self)
    
    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь', related_name='carts')
    session_key = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = CartQuery.as_manager()
    
    def __str__(self):
        if self.user:
            return f'Корзина пользователя | {self.user.username} | Товар: {self.product.category} {self.product.title}'
        else:
            return f'Корзина "Анонимного" пользователя | Товар: {self.product.category} {self.product.title}'
    
    @property
    def products_price(self):
        return round(self.product.price - self.product.price*self.product.discount/100) * self.quantity


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        
        
    
    
    
    


