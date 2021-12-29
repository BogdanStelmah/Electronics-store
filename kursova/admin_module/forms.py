from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    image = forms.ImageField()
    description = forms.TextInput()
    price = forms.CharField(max_length=4)



class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть ім\'я'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть призвище'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Введіть логін'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введіть пошту'}))