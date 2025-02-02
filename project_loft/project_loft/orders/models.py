from django.db import models

from goods.models import Product
from users.models import User

# Create your models here.


class OrderItemQuery(models.QuerySet):
    
    def total_price(self):
        return sum(order.product_sell_price for order in self)
    
    def total_quantity(self):
        return sum(order.product_quantity for order in self)
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='orders', null=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя получателя', null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия получателя', null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    city = models.CharField(max_length=70, verbose_name='Город', null=True)
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    requires_delivery = models.CharField(max_length=20, verbose_name='Требуется доставка')
    payment_method = models.CharField(max_length=20, verbose_name='Способ оплаты', blank=True, null=True)
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default='В обработке', verbose_name="Статус заказа")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание заказа')
    
    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("id",)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='order_products', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Продукт', null=True)   
    product_title = models.CharField(max_length=150, verbose_name='Название товара')
    product_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, verbose_name='Цена товара')
    product_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    product_category = models.CharField(max_length=150, verbose_name='Категория товара')
    product_color_name_en = models.CharField(max_length=150, verbose_name='Цвет товара', null=True)
    
    
    def __str__(self):
        return f'{self.product_title}'
    
    objects = OrderItemQuery.as_manager()

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'
        
    @property
    def product_sell_price(self):
        return round(self.product.price - self.product.price*self.product.discount/100) * self.product_quantity
    





