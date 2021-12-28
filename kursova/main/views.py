# from django.contrib import messages

from django.shortcuts import render, redirect

from .models import Product


# @login_required(login_url='login')
def index(request):
    product = Product.objects.order_by('-name')  # сортує по імені, all() виводить всі записи (- це ревьорс) ([:1] - виводить 1 запис)
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'product': product})

