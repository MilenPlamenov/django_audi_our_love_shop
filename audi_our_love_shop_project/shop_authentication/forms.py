from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

ShopUser = get_user_model()


class RegisterUsers(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('email', 'password1', 'password2')

