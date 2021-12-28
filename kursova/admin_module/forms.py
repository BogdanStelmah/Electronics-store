from django.forms import ModelForm, TextInput
from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.ImageField()
    price = forms.CharField(max_length=4)