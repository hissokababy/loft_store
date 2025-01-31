# Generated by Django 4.2.12 on 2025-01-25 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_category_sub_category_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название товара')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена товара')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка на товар')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Товара в наличии')),
                ('size', models.CharField(max_length=30, verbose_name='Размер товара')),
                ('color_name', models.CharField(default='Белый', max_length=150, verbose_name='Цвет товара')),
                ('color_code', models.CharField(default='#FFFFFF', max_length=10, verbose_name='Код цвета товара')),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='Рейтинг товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Фото товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фото товара',
            },
        ),
    ]
