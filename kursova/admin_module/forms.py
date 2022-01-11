from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'discount', 'number', 'categories']
        widgets = {
            'discount': forms.NumberInput,
            'number': forms.NumberInput,
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        try:
            price = float(price)
            if price < 0:
                raise ValidationError("Ціна неможе бути від\'ємною")
        except ValueError:
            try:
                price = int(price)
                if price < 0:
                    raise ValidationError("Ціна неможе бути від\'ємною")
            except ValueError:
                raise ValidationError("Невірно вказана ціна")

        return round(price, 2)

    def clean_discount(self):
        discount = self.cleaned_data['discount']

        try:
            discount = int(discount)
        except ValueError:
            raise ValidationError("Невірно вказана знижка")

        if discount < 0 or discount > 100:
            raise ValidationError("Невірно вказана знижка")

        return discount

    def clean_number(self):
        number = self.cleaned_data['number']
        error = ValidationError("Невірно вказана кількість")

        try:
            number = int(number)
        except ValueError:
            raise error

        if number < 0:
            raise error

        return number


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть ім\'я'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть призвище'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть логін'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введіть пошту'}))


class EditSuperUserForm(EditUserForm):
    is_superuser = forms.BooleanField(required=False)
