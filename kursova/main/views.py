from django.shortcuts import render
from django.core import serializers
from .models import Product, ProductCategory, Basket
from django.http import JsonResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def basket_count(request):
    basket_count = 0
    if request.user.is_authenticated:
        basket_items = Basket.objects.filter(user=request.user)
        for i in range(len(basket_items)):
            basket_count += basket_items[i].quantity

    return basket_count


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

        products = serializers.serialize("json", products[:int(request.GET.get('count_show'))])

        return JsonResponse(products, safe=False)
    else:
        products = Product.objects.all()[:2]

    categories = ProductCategory.objects.all()

    context = {
        'title': 'Головна сторінка сайту',
        'products': products,
        'categories': categories,
        'basket_count': basket_count(request)
    }

    return render(request, 'main/index.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'title': 'Головна сторінка сайту',
        'product': product,
        'basket_count': basket_count(request)
    }

    return render(request, 'main/product.html', context)