from django.contrib import admin

from orders.models import Order, OrderItem

# Register your models here.


class OrderItemTabular(admin.TabularInline):
    model = OrderItem
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabular,]