from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Product
from .forms import RegistrationForm, LoginForm, ProductForm


# @login_required(login_url='login')
def index(request):
    product = Product.objects.order_by('-name')  # сортує по імені, all() виводить всі записи (- це ревьорс) ([:1] - виводить 1 запис)
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'product': product})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Невірний логін або пароль')

        form = LoginForm()
        context = {
            'form': form,
            'title': 'Авторизація'
        }

    return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        error = ''
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegistrationForm()  # сттандартна форма реєстрації Django

        context = {
            'form': form,
            'error': error,
            'title': 'Реєстрація'
        }

        return render(request, 'main/register.html', context)


def create_product(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        error = ''
        if request.method == 'POST':  # передаються данні якщо метод пост
            form = ProductForm(request.POST)  # отримуємо данні
            if form.is_valid():  # перевіряємо на коретність
                # form.save()
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
        return render(request, 'main/create_product.html', context)