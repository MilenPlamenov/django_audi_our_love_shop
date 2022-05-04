from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ManyToManyField

ShopUser = get_user_model()


class Product(models.Model):
    TITLE_MAX_LENGTH = 50
    CATEGORY_MAX_LENGTH = 50
    PART = 'Part'
    CAR_CARE = 'Car care'
    ACCESSORY = 'Accessory'
    CATEGORY_CHOICES = (
        (PART, PART),
        (CAR_CARE, CAR_CARE),
        (ACCESSORY, ACCESSORY),

    )
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    price = models.FloatField()
    description = models.TextField(
        blank=True,
        null=True,
        default='No description',
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=CATEGORY_MAX_LENGTH,
        default=PART,
    )

    def __str__(self):
        return self.title


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField(
        default=1,
    )


class Order(models.Model):
    user = models.ForeignKey(
        ShopUser,
        on_delete=models.CASCADE,
    )

    items = ManyToManyField(OrderProduct)

    start_date = models.DateTimeField(
        auto_now_add=True,
    )

    ordered_date = models.DateTimeField()

    ordered = models.BooleanField(
        default=False,
    )
