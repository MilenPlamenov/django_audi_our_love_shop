from django.contrib.auth.views import LogoutView
from django.urls import path

from audi_our_love_shop_project.shop_authentication.views import CreateAccount

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='create account'),
    path('logout/', LogoutView.as_view(), name="logout"),
]
