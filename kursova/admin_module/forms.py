from django import forms
from django.forms import ModelForm
from main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "description", "price", "discount", "number", "categories"]


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть ім\'я'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть призвище'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть логін'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введіть пошту'}))