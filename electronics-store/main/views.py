from django.shortcuts import render, redirect
from django.core import serializers
from django.urls import reverse

from .forms import ReviewsForm
from .models import Product, ProductCategory, Basket, ReviewsProduct
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound


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

        try:
            products = serializers.serialize("json", products[:int(request.GET.get('count_show')) + 1])
        except ValueError:
            return redirect('login')

        return JsonResponse(products, safe=False)
    else:
        products = Product.objects.all()[:10]

    categories = ProductCategory.objects.all()

    context = {
        'title': 'Головна сторінка сайту',
        'products': products,
        'categories': categories,
        'basket_count': basket_count(request),
    }

    return render(request, 'main/index.html', context)


def product(request, pk):
    if request.method == "POST":
        form = ReviewsForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = Product.objects.get(id=pk)
            form.save()

        return HttpResponseRedirect(reverse('product', args=(pk,)))

    product = Product.objects.get(id=pk)
    reviews = ReviewsProduct.objects.filter(product=product)

    form = ReviewsForm()

    context = {
        'title': 'Головна сторінка сайту',
        'product': product,
        'basket_count': basket_count(request),
        'reviews': reviews,
        'form': form
    }

    return render(request, 'main/product.html', context)


def delete_reviews(request, pk, pk_review):
    if not request.user.is_authenticated:
        return redirect('home')

    try:
        reviews = ReviewsProduct.objects.get(id=pk_review)
        if request.user == reviews.user:
            reviews.delete()
        else:
            return redirect('home')

        return HttpResponseRedirect(reverse('product', args=(pk,)))

    except ProductCategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого коментарю не існує</h2>")