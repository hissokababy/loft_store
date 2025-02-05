from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction
from orders.forms import OrderForm
from orders.models import Order, OrderItem

# Create your views here.


def checkout(request):
    if request.method == 'GET':
        form = OrderForm()   
    else:
            form = OrderForm(data=request.POST)
            if form.is_valid:
                print(form.data)
                try:
                    with transaction.atomic():
                        user_carts = request.user.carts.all()
                        
                        if user_carts.exists():
                            
                            order = Order.objects.create(
                                user=request.user,
                                first_name=form.data['first_name'],
                                last_name=form.data['last_name'],
                                phone_number=form.data['phone_number'],
                                city=form.data['city'],
                                delivery_address=form.data['delivery_address'],
                                requires_delivery=form.data['requires_delivery'],
                                payment_method=form.data['payment_method'],                            
                            )

                            for i in user_carts:
                                product=i.product
                                title=i.product.title
                                price=i.products_price
                                quantity=i.quantity
                                category=i.product.category
                                color=i.product.color_name_en
                            
                            
                                if product.quantity < quantity:
                                    raise ValidationError(f'Недостаточное количество товара {title} на складе\
                                                        В наличии - {product.quantity}')
                                
                                
                                OrderItem.objects.create(
                                    order=order,
                                    product=product,
                                    product_title=title,
                                    product_price=price,
                                    product_quantity=quantity,
                                    product_category=category,
                                    product_color_name_en=color,
                                )
                                product.quantity -= quantity
                                product.save()
                                
                            user_carts.delete()
                            messages.success(request, 'Заказ офомлен!')
                            return redirect('users:profile')
                    
                except ValidationError as e:
                    messages.success(request, str(e))
                    return redirect('carts:order')

            else:
                messages.error(request, 'Неверный формат данных')
                return redirect('orders:order')
        
    context = {
        'user_carts': request.user.carts.all(),
        'form': form
    }
    return render(request, 'orders/checkout.html', context)



def order_products_view(request):
    if request.user.is_authenticated:
        user_orders = request.user.orders.all()
        context = {
            'user_orders': user_orders,
        }
            
        return render(request, 'orders/order_products.html', context)
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))