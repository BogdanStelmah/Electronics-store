from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User

from admin_module.forms import EditUserForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            form = LoginForm(request.POST)
            form.add_error('username', "Невірний логін або пароль")
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Авторизація'
    }

    return render(request, 'user_module/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()  # сттандартна форма реєстрації Django

    context = {
        'form': form,
        'title': 'Реєстрація'
    }

    return render(request, 'user_module/register.html', context)


def account(request):
    if not request.user.is_authenticated:
        return redirect('home')

    context = {
        'user': request.user,
        'title': 'Акаунт'
    }

    return render(request, 'user_module/account.html', context)


def edit_account(request, id):
    if not request.user.is_authenticated or request.user.id != id:
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

                messages.add_message(request, messages.INFO, 'Акаунт оновлено')

                return redirect('home')
        else:
            form = EditUserForm(initial={'first_name': user.first_name,
                                         'last_name': user.last_name,
                                         'username': user.username,
                                         'email': user.email,
                                         })

        context = {
            'title': 'Оновлення інформації',
            'form': form
        }
        return render(request, 'user_module/edit_account.html', context)

    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого користувача не існує</h2>")