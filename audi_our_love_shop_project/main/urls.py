from django.urls import path

from audi_our_love_shop_project.main.views import index

urlpatterns = [
    path('', index, name='index')
]
