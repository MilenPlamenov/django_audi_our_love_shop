from django import forms

from audi_our_love_shop_project.shop.models import BillingAddress


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'second_address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'custom-select d-block w-100',
                }
            ),
            'zip_code': forms.TextInput(
                attrs={
                    'class': 'form-control custom-select d-block w-100',
                }
            ),
        }
