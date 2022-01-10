from django.shortcuts import render, redirect
from django.core import serializers
from main.models import ProductCategory, Product, Basket
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib import messages


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# Create your views here.
def basket(request):
    if is_ajax(request):
        pass

    basket = Basket.objects.all()

    context = {
        'title': 'Корзіна',
        'basket': basket
    }

    return render(request, 'basket_module/basket.html', context)


def add_item_basket(request, pk):
    basket = Basket.objects.filter(user=request.user, product__id=pk).first()
    if basket:
        basket.quantity += 1
        basket.save()
    else:
        try:
            product = Product.objects.get(id=pk)

            basket = Basket(user=request.user, product=product)
            basket.quantity += 1
            basket.save()
        except Product.DoesNotExist:
            return HttpResponseNotFound("<h2>Такого товару не існує</h2>")

    return redirect('home')


def delete_item_basket(request, pk):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        basket = Basket.objects.get(id=pk)

        messages.add_message(request, messages.INFO, 'Товар ' + str(basket.product.name) + ' видалено')
        basket.delete()

        return redirect('basket')
    except ProductCategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого товару не існує</h2>")