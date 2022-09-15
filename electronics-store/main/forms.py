from django.forms import ModelForm, TextInput
from django import forms
from .models import ReviewsProduct


class ReviewsForm(ModelForm):
    class Meta:
        model = ReviewsProduct
        fields = ['reviews']
