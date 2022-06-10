# Generated by Django 4.0.4 on 2022-06-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refunded',
            field=models.BooleanField(default=False),
        ),
    ]
