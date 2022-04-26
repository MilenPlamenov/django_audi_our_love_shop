from django.urls import path

from audi_our_love_shop_project.contacts.views import contacts

urlpatterns = [
    path('', contacts, name='contacts'),
]