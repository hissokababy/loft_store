from django.contrib import admin
from django.utils.safestring import mark_safe
from goods.models import Category, Product, ProductImage
from goods.forms import GetIcon

# Register your models here.


class ProductImageTabular(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = GetIcon
    list_display = ('title', 'get_icon_category')
    
    
    def get_icon_category(self, obj):
        try:
            if obj.image:
                return mark_safe(f'<img src="{obj.image.url}" width="40">')
            else:
                return None
        except:
            return None
        
    get_icon_category.short_description = 'Иконка категории'
    
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ( 'title', 'color_name_en')}
    inlines = [ProductImageTabular, ]
    