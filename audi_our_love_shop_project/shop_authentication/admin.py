from django.contrib import admin

from audi_our_love_shop_project.shop_authentication.forms import ShopUser


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    pass
