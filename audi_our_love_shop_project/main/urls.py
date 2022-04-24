from django.urls import path

from audi_our_love_shop_project.main.views import index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
