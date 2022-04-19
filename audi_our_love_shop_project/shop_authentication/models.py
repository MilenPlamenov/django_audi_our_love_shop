from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from audi_our_love_shop_project.shop_authentication.manager import ShopUserManager


# should be made in the beginning of the project!
class ShopUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'email'  # will use email as username

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = ShopUserManager()
