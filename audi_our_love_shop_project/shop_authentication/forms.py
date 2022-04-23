from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

ShopUser = get_user_model()


class RegisterUsers(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUsers, self).__init__(*args, **kwargs)
        for field_name in ['email', 'password1', 'password2']:
            self.fields[field_name].help_text = None

        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Enter password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Confirm password"})


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))