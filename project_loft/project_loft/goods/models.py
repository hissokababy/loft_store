from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to='icons/categories/', verbose_name='Иконка категории', blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("goods:catalog", kwargs={"category_slug": self.slug})
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    
    
class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название товара')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, verbose_name='Цена товара')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка на товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Товара в наличии')
    size = models.CharField(max_length=130, verbose_name='Размер товара')
    color_name_ru = models.CharField(default='Белый', verbose_name='Цвет товара ru', max_length=150)
    color_name_en = models.CharField(default='White', verbose_name='Цвет товара en', max_length=150)
    color_code = models.CharField(default='#FFFFFF', verbose_name='Код цвета товара', max_length=10)
    rating = models.DecimalField(default=0.0, max_digits=2, decimal_places=1, verbose_name='Рейтинг товара')
    
    
    def __str__(self):
        return f'{self.category.title} {self.title} {self.color_name_en}'
    
    def get_absolute_url(self):
        return reverse("goods:product", kwargs={"product_slug": self.slug})
    
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-id',)

    def get_product_image(self):
        if self.images:
            return self.images.all().first().image.url
        else:
            return None
        
        
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100)
        else:
            return self.price

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Фото товара')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')
    
    
    def __str__(self):
        return f'Фото товара'
    
    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'