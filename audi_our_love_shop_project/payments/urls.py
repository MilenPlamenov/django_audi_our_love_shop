from django.urls import path

from audi_our_love_shop_project.payments.views import stripe_payment_view

urlpatterns = [
    path('stripe/', stripe_payment_view, name='stripe-payment'),
]
