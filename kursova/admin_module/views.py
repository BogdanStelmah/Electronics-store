from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import ProductForm, EditUserForm
from main.models import ProductCategory, Product


def create_product(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        error = ''
        if request.method == 'POST':  # передаються данні якщо метод пост
            form = ProductForm(request.POST, request.FILES)  # отримуємо данні

            if form.is_valid():  # перевіряємо на коретність
                try:
                    Product.objects.create(**form.cleaned_data)
                    return redirect('home')
                except:
                    error = 'Помилка'
            else:
                error = 'Невірна форма'
        else:
            form = ProductForm()

        context = {
            'form': form,
            'error': error
        }
        return render(request, 'admin_module/create_product.html', context)


def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        context = {
            'title': 'Адмін панель'
        }
        return render(request, 'admin_module/admin_panel.html', context)


def users_db(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        users = User.objects.all()
        context = {
            'title': 'Користувачі',
            'users': users
        }
        return render(request, 'admin_module/users.html', context)


def delete_user(request, id):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        try:
            user = User.objects.get(id=id)
            user.delete()
            return redirect('users_db')
        except User.DoesNotExist:
            return HttpResponseNotFound("<h2>Такого користувача не існує</h2>")


def edit_user(request, id):
    if not request.user.is_superuser:
        return redirect('home')
    else:
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
    else:
        categories = ProductCategory.objects.all()
        context = {
            'title': 'Категорії',
            'categories': categories
        }
        return render(request, 'admin_module/category.html', context)


def add_category(request):
    return None


def product_db(request):
    return None


def add_product(request):
    return None