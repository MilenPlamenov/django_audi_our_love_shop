from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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
        'order': order,
    }
    total = 0
    total_items_count = 0
    total = order_details(order, context, total, total_items_count)
    if request.method == 'POST':
        try:
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

            order_items = order.items.all()
            order_items.update(ordered=True)
            for item in order_items:
                item.save()

            order.ordered = True
            order.payment = payment
            order.save()
            messages.success(request, 'Thank you for your order !')
            return redirect(reverse('home'))

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.warning(request, f"{err.get('message')}")
            return redirect(reverse('home'))

        except stripe.error.RateLimitError as e:
            messages.warning(request, "Rate limit error")
            return redirect(reverse('home'))

        except stripe.error.InvalidRequestError as e:
            messages.warning(request, "Invalid parameters")
            return redirect(reverse('home'))

        except stripe.error.AuthenticationError as e:
            messages.warning(request, "Not authenticated")
            return redirect(reverse('home'))

        except stripe.error.APIConnectionError as e:
            messages.warning(request, "Network error")
            return redirect(reverse('home'))

        except stripe.error.StripeError as e:
            messages.warning(
                request, "Something went wrong. Please try again !")
            return redirect(reverse('home'))

        except Exception as e:
            # demo of sending email to the tech support to fix it
            send_mail(
                str(e),
                'Must fix this!',
                from_email='from@example.com',
                recipient_list=['to@example.com'],
                fail_silently=False,
            )
            messages.warning(
                request, "A serious error occurred.")
            return redirect(reverse('home'))

    return render(request, 'payments/stripe_payments.html', context)
