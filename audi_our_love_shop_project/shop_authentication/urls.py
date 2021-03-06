from django.contrib.auth.views import LogoutView
from django.urls import path

from audi_our_love_shop_project.shop_authentication.views import CreateAccount, LoginAccount, AccountDetailsView

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='create account'),
    path('login/', LoginAccount.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('account-details/<int:pk>/', AccountDetailsView.as_view(), name='account-details'),
]
