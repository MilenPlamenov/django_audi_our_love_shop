from django.urls import path

from audi_our_love_shop_project.shop.views import home, product, checkout

urlpatterns = [
    path('home/', home, name='home'),
    path('product/', product, name='product'),
    path('checkout/', checkout, name='checkout'),
]