from django.shortcuts import render, redirect, get_object_or_404
from products.models import Coffee
from .models import CartItem
# Create your views here.

def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, coffee=coffee)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('coffee_list')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})
