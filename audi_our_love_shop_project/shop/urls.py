from django.urls import path

from audi_our_love_shop_project.shop.views import home, checkout, ProductDetailView

urlpatterns = [
    path('home/', home, name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),
]