from django.contrib import admin

from orders.models import Order
from users.models import User

# Register your models here.

class UserCartProductsTabular(admin.TabularInline):
    model = Order
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [UserCartProductsTabular, ]