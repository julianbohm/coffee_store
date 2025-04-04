from django.shortcuts import render, redirect, get_object_or_404
from products.models import Coffee
from .models import CartItem
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, coffee=coffee)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('coffee_list')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        new_qty = int(request.POST.get('quantity', 1))
        if new_qty > 0:
            item.quantity = new_qty
            item.save()
        else:
            item.delete()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')
