from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from main.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'mail_address']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Введіть телефон', 'required': True}),
            'mail_address': forms.TextInput(attrs={'placeholder': 'Введіть адресу', 'required': True})
        }