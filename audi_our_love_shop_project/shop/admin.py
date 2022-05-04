from django.contrib import admin

from audi_our_love_shop_project.shop.models import Product, OrderProduct, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

