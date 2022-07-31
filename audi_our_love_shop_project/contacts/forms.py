from django import forms

from audi_our_love_shop_project.contacts.models import ContactsModel


class ContactsForm(forms.ModelForm):
    class Meta:
        model = ContactsModel
        fields = ('first_name', 'last_name', 'email', 'reason', 'content')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'reason': forms.Select(choices=ContactsModel.CONTACT_CHOICES, attrs={'class': 'form-control'}),
        }