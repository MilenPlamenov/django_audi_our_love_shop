from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from audi_our_love_shop_project.payments.models import StripePayments
from audi_our_love_shop_project.settings import env
from audi_our_love_shop_project.shop.models import Order
from audi_our_love_shop_project.shop.helpers import order_details
import stripe

stripe.api_key = env('STRIPE_API_KEY')


@login_required
def stripe_payment_view(request):
    order = Order.objects.get(user=request.user, ordered=False)
    context = {
        'order': order
    }
    total = 0
    total_items_count = 0
    total = order_details(order, context, total, total_items_count)
    if request.method == 'POST':
        customer = stripe.Customer.create(
            email=request.user.email,
            source=request.POST['stripeToken'],
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=int(total) * 100,
            currency='usd',
            description=f'Order id: {order.pk}.'
                        f' Ordered by: {request.user.email}.'
                        f'Products: {[p.product.title for p in order.items.all()]}.',
        )

        payment = StripePayments()
        payment.stripe_charge_id = charge['id']
        payment.user = request.user
        payment.total = total
        payment.save()

        order.ordered = True
        order.payment = payment
        order.save()
        messages.success(request, 'Thank you for your order !')
        return redirect(reverse('home'))

    return render(request, 'payments/stripe_payments.html', context)
