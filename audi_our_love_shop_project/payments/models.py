from django.contrib.auth import get_user_model
from django.db import models

ShopUser = get_user_model()


class StripePayments(models.Model):
    CHARGE_ID_MAX_LENGTH = 100

    stripe_charge_id = models.CharField(
        max_length=CHARGE_ID_MAX_LENGTH,
    )

    user = models.ForeignKey(
        ShopUser,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    total = models.FloatField()

    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Stripe payment for {self.user}. Price: {self.total} on {self.timestamp}'

