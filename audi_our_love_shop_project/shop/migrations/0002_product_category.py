# Generated by Django 4.0.4 on 2022-05-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Part', 'Part'), ('Car care', 'Car care'), ('Accessory', 'Accessory')], default='Part', max_length=50),
        ),
    ]
