import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderItem

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('coffee_list')

    order = Order.objects.create(user=request.user)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            coffee=item.coffee,
            quantity=item.quantity
        )

    line_items = []
    for item in cart_items:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.coffee.name,
                },
                'unit_amount': int(item.coffee.price * 100),
            },
            'quantity': item.quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/checkout/success/'),
        cancel_url=request.build_absolute_uri('/cart/view/'),
    )

    order.stripe_payment_intent = session.payment_intent
    order.save()
    cart_items.delete()

    return redirect(session.url, code=303)

def checkout_success(request):
    return render(request, 'checkout/success.html')

