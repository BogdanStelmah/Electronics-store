from django.shortcuts import render
from django.core import serializers
from .models import Product, ProductCategory
from django.http import JsonResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    if is_ajax(request):
        try:
            price__from = int(request.GET.get("price__from"))
            price__to = int(request.GET.get("price__to"))
        except ValueError:
            price__from = 0
            price__to = 99999

        products = Product.objects.all()

        if request.GET.getlist("category[]"):
            products = products.filter(categories__name__in=request.GET.getlist("category[]"))

        if request.GET.get("search"):
            products = products.filter(name__icontains=request.GET.get("search"))

        if request.GET.get("price__from") and request.GET.get("price__to"):
            products = products.filter(discounted_price__range=(price__from, price__to))

        products = serializers.serialize("json", products)

        return JsonResponse(products, safe=False)
    else:
        products = Product.objects.all()

    categories = ProductCategory.objects.all()

    context = {
        'title': 'Головна сторінка сайту',
        'products': products,
        'categories': categories
    }

    return render(request, 'main/index.html', context)