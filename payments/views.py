from django.shortcuts import get_object_or_404, render
from .models import Item, Order

import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def get_stripe_keys(currency):
    if currency == 'eur':
        return settings.STRIPE_SECRET_KEY_EUR, settings.STRIPE_PUBLISHABLE_KEY_EUR
    return settings.STRIPE_SECRET_KEY_USD, settings.STRIPE_PUBLISHABLE_KEY_USD

@csrf_exempt
def create_payment_intent(request, id):
    item = Item.objects.get(id=id)
    secret_key, _ = get_stripe_keys(item.currency)
    stripe.api_key = secret_key

    intent = stripe.PaymentIntent.create(
        amount=int(item.price * 100),  # в центах
        currency=item.currency,
        metadata={"item_id": item.id},
    )

    return JsonResponse({'clientSecret': intent.client_secret})

def item_view(request, id):
    item = Item.objects.get(id=id)
    _, public_key = get_stripe_keys(item.currency)
    return render(request, 'item.html', {
        'item': item,
        'stripe_public_key': public_key
    })

def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)
    secret_key, _ = get_stripe_keys(item.currency)
    stripe.api_key = secret_key

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    return JsonResponse({'id': session.id})

def order_view(request, id):
    order = get_object_or_404(Order, pk=id)
    _, public_key = get_stripe_keys(order.currency())
    return render(request, 'order.html', {
        'order': order,
        'stripe_public_key': public_key
    })

def buy_order(request, id):
    order = get_object_or_404(Order, pk=id)
    currency = order.currency()
    secret_key, _ = get_stripe_keys(currency)
    stripe.api_key = secret_key

    line_items = []
    for item in order.items.all():
        line_items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        })

    discounts = []
    if order.discount:
        coupon = stripe.Coupon.create(
            percent_off=float(order.discount.percentage),
            duration='once',
        )
        discounts.append({'coupon': coupon.id})

    tax_rates = []
    if order.tax:
        tax = stripe.TaxRate.create(
            display_name=order.tax.name,
            percentage=float(order.tax.percentage),
            inclusive=False,
        )
        tax_rates.append(tax.id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        discounts=discounts if discounts else None,
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    return JsonResponse({'id': session.id})