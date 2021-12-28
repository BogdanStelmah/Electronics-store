from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm


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

    return render(request, 'user_module/login.html', context)


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

        return render(request, 'user_module/register.html', context)
