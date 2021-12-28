from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import ProductForm


def create_product(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        error = ''
        if request.method == 'POST':  # передаються данні якщо метод пост
            form = ProductForm(request.POST, request.FILES)  # отримуємо данні

            if form.is_valid():  # перевіряємо на коретність
                # form.save()
                try:
                    from kursova.main.models import Product
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

            if request.POST == "POST":
                user.update(request.POST)
                return redirect('users_db')
            else:
                context = {
                    'title': 'Оновлення інформації'
                }
                return render(request, 'admin_module/admin_panel.html', context)
        except User.DoesNotExist:
            return HttpResponseNotFound("<h2>Такого користувача не існує</h2>")


