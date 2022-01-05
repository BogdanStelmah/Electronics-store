# from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Product, ProductCategory


# @login_required(login_url='login')
def index(request):
    if not request.GET.getlist("category"):
        if request.GET.get("search") is None:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(name__icontains=request.GET.get("search"))
    else:
        if request.GET.get("search") is None:
            products = Product.objects.filter(categories__name__in=request.GET.getlist("category"))
        else:
            products = Product.objects.filter(
                Q(categories__name__in=request.GET.getlist("category")),
                Q(name__icontains=request.GET.get("search"))
            )

    categories = ProductCategory.objects.all()

    context = {
        'title': 'Головна сторінка сайту',
        'products': products,
        'categories': categories
    }

    return render(request, 'main/index.html', context)