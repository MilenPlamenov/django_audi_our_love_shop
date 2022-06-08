from django.contrib import admin

from audi_our_love_shop_project.payments.models import StripePayments


@admin.register(StripePayments)
class StripePaymentsAdmin(admin.ModelAdmin):
    pass
