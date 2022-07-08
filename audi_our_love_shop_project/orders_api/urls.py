from django.urls import path

from audi_our_love_shop_project.orders_api.views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView, \
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('order-list-create/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order-retrieve-update-destroy/<str:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(),
         name='order-retrieve-update-destroy'),

    path('product-list-create/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('product-retrieve-update-destroy/<str:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='product-retrieve-update-destroy'),
]
