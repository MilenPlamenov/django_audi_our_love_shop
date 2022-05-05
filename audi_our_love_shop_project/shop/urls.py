from django.urls import path

from audi_our_love_shop_project.shop.views import home, checkout, ProductDetailView, add_to_cart, remove_from_cart, \
    remove_single_item_from_cart

urlpatterns = [
    path('home/', home, name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<int:pk>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
