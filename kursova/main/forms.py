from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, TextInput
from django import forms


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть ім\'я'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть призвище'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть логін'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введіть пошту'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть логін'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль'}))


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.ImageField()
    price = forms.CharField(max_length=4)
