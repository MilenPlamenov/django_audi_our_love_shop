from django.contrib.auth import get_user_model
from django.test import Client


class UserAndClientCreateMixin:
    ModelUser = get_user_model()
    VALID_USER_CREDENTIALS = {
        'email': 'test1@emample.com',
        'password': '12345qwe',
    }

    def __init__(self):
        self.email = self.VALID_USER_CREDENTIALS['email']
        self.password = self.VALID_USER_CREDENTIALS['password']

    def login(self):
        user = self.ModelUser.objects.create_user(email=self.email)
        user.set_password(self.password)
        user.save()
        client = Client()
        client.login(email=self.email, password=self.password)
        return user, client
