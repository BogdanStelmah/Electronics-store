from django.shortcuts import render, redirect
from django.core import serializers
from django.urls import reverse
from main.models import ProductCategory, Product, Basket
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib import messages


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# Create your views here.
def basket(request):
    if not request.user.is_authenticated:
        return redirect('home')

    basket = Basket.objects.filter(user=request.user)

    sum_price = 0
    for i in range(len(basket)):
        sum_price += basket[i].product.discounted_price * basket[i].quantity

    context = {
        'title': 'Кошик',
        'basket': basket,
        'sum_price': round(sum_price, 2),
    }

    return render(request, 'basket_module/basket.html', context)


def add_item_basket(request, pk):
    add_items(request, pk)

    return redirect('home')


def add_item_basket_product(request, pk):
    add_items(request, pk)

    return HttpResponseRedirect(reverse('product', args=(pk,)))


def add_items(request, pk):
    if not request.user.is_authenticated:
        return redirect('register')

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


def delete_item_basket(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    try:
        basket = Basket.objects.get(id=pk)

        messages.add_message(request, messages.INFO, 'Товар ' + str(basket.product.name) + ' видалено')
        basket.delete()

        return redirect('basket')
    except ProductCategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого товару не існує</h2>")


def create_order(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if request.method == "GET":
        basket = Basket.objects.filter(user=request.user)

        count = 0
        for i in range(len(basket)):
            if basket[i].quantity <= basket[i].product.number:
                pass
            else:
                count += 1
                messages.add_message(request, messages.ERROR, "Товару під назвою '"
                                     + str(basket[i].product.name)
                                     + "' на складі залишилось "
                                     + str(basket[i].product.number) + " шт")

        if count == 0:
            for i in range(len(basket)):
                product = Product.objects.get(id=basket[i].product.id)
                product.number -= basket[i].quantity
                product.save()

            basket.delete()
            messages.add_message(request, messages.INFO, "Замовлення відправленно")

            return redirect('home')

    return redirect('basket')


def remove_quantity(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    basket = Basket.objects.get(id=pk)

    if basket.quantity != 1:
        basket.quantity -= 1
        basket.save()

    return redirect('basket')


def add_quantity(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')

    basket = Basket.objects.get(id=pk)
    basket.quantity += 1
    basket.save()

    return redirect('basket')
