from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import ProductForm, EditUserForm, CategoryForm
from main.models import ProductCategory, Product


def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('home')

    context = {
        'title': 'Адмін панель'
    }
    return render(request, 'admin_module/admin_panel.html', context)


def users_db(request):
    if not request.user.is_superuser:
        return redirect('home')

    users = User.objects.all()
    context = {
        'title': 'Користувачі',
        'users': users
    }
    return render(request, 'admin_module/users.html', context)


def delete_user(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        user = User.objects.get(id=id)
        user.delete()
        return redirect('users_db')
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого користувача не існує</h2>")


def edit_user(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        user = User.objects.get(id=id)
        if request.method == "POST":
            form = EditUserForm(request.POST)

            login = User.objects.filter(username=request.POST.get("username"))
            if len(login) >= 1 and str(user.username) != str(login[0]):
                form.add_error('username', "Такий логін вже існує")

            if form.is_valid():
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.username = request.POST.get("username")
                user.email = request.POST.get("email")
                user.save()

                messages.add_message(request, messages.INFO, 'Користувача ' + user.username + ' оновлено')

                return redirect('users_db')
        else:
            form = EditUserForm

        context = {
            'title': 'Оновлення інформації',
            'user': user,
            'form': form
        }
        return render(request, 'admin_module/edit_user.html', context)

    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого користувача не існує</h2>")


def category_db(request):
    if not request.user.is_superuser:
        return redirect('home')

    categories = ProductCategory.objects.all()
    context = {
        'title': 'Категорії',
        'categories': categories
    }
    return render(request, 'admin_module/category.html', context)


def add_category(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == "POST":
        form = CategoryForm(request.POST)  # отримуємо данні

        name_category = ProductCategory.objects.filter(name=request.POST.get('name'))
        if len(name_category) >= 1 and request.POST.get('name') != name_category[0]:
            form.add_error('name', "Така категорія вже існує")

        if form.is_valid():
            messages.add_message(request, messages.INFO, 'Додано нову категорію ')
            ProductCategory.objects.create(**form.cleaned_data)
            return redirect('category_db')
    else:
        form = CategoryForm

    context = {
        'title': "Додавання категорії",
        'form': form,
    }
    return render(request, 'admin_module/add_category.html', context)


def delete_category(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        category = ProductCategory.objects.get(id=id)
        messages.add_message(request, messages.INFO, 'Категорію ' + str(category) + ' видалено')
        category.delete()
        return redirect('category_db')
    except ProductCategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Такої категорії не існує</h2>")


def edit_category(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        category = ProductCategory.objects.get(id=id)
        if request.method == "POST":
            form = CategoryForm(request.POST)

            name_category = ProductCategory.objects.filter(name=request.POST.get("name"))
            if len(name_category) >= 1 and str(category.name) != str(name_category[0]):
                form.add_error('name', "Така категорія вже існує")

            if form.is_valid():
                category.name = request.POST.get("name")
                category.save()

                messages.add_message(request, messages.INFO, 'Категорію ' + category.name + ' оновлено')

                return redirect('category_db')
        else:
            form = CategoryForm

        context = {
            'title': 'Оновлення інформації',
            'category': category,
            'form': form
        }
        return render(request, 'admin_module/edit_category.html', context)

    except ProductCategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Такогої категорії не існує</h2>")


def product_db(request):
    product = Product.objects.order_by('-name')
    return render(request, 'admin_module/products.html', {'title': 'Товари', 'products': product})


def add_product(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)

            price = request.POST.get('price')
            discount = request.POST.get('discount')

            discounted_price = float(price) - ((float(price) / 100) * int(discount))
            post.discounted_price = round(discounted_price, 2)
            post.save()

            return redirect('product_db')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'admin_module/add_product.html', context)


def delete_product(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        product = Product.objects.get(id=id)

        messages.add_message(request, messages.INFO, 'Товар ' + str(product.name) + ' видалено')
        product.delete()

        return redirect('product_db')
    except ProductCategory.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого товару не існує</h2>")


def edit_product(request, id):
    if not request.user.is_superuser:
        return redirect('home')

    try:
        product = Product.objects.get(id=id)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                post = form.save(commit=False)

                price = request.POST.get('price')
                discount = request.POST.get('discount')

                discounted_price = float(price) - ((float(price) / 100) * int(discount))
                post.discounted_price = round(discounted_price, 2)
                post.save()

                messages.add_message(request, messages.INFO, 'Товар ' + str(product.name) + ' оновлено')
                return redirect('product_db')
        else:
            form = ProductForm(initial={'name': product.name,
                                        'image': product.image,
                                        'description': product.description,
                                        'price': product.price,
                                        'discount': product.discount,
                                        'number': product.number,
                                        'categories': product.categories})

        context = {
            'title': 'Оновлення інформації',
            'form': form
        }
        return render(request, 'admin_module/edit_product.html', context)

    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого товару не існує</h2>")