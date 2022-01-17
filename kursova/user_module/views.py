from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import User

from admin_module.forms import EditUserForm

from main.models import Profile, OrderItems, Order, Product

from django.db.models import Count


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
            user = form.save()

            profile = Profile(user=user)
            profile.save()

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

    orders_and_item = []
    orders = Order.objects.filter(user=request.user).order_by('order_status')

    for i in range(orders.count()):
        sum_price = 0
        items = OrderItems.objects.filter(order=orders[i])

        for j in range(items.count()):
            sum_price += items[j].product.discounted_price * items[j].quantity

        orders_and_item.append({"id": orders[i].id,
                                "status": orders[i].order_status,
                                "sum_price": sum_price,
                                "items": items
                                })

    context = {
        'user': Profile.objects.get(user=request.user),
        'title': 'Акаунт',
        'orders': orders_and_item
    }
    print(type(context))

    return render(request, 'user_module/account.html', context)


def edit_account(request, id):
    if not request.user.is_authenticated or request.user.id != id:
        return redirect('home')

    try:
        user = User.objects.get(id=id)
        profile = Profile.objects.get(user=user)

        if request.method == "POST":
            form = EditUserForm(request.POST)
            form_profile = ProfileForm(request.POST)

            login = User.objects.filter(username=request.POST.get("username"))
            if len(login) >= 1 and str(user.username) != str(login[0]):
                form.add_error('username', "Такий логін вже існує")

            if form.is_valid() and form_profile.is_valid():
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.username = request.POST.get("username")
                user.email = request.POST.get("email")
                user.save()

                profile.phone_number = request.POST.get("phone_number")
                profile.mail_address = request.POST.get("mail_address")
                profile.save()

                messages.add_message(request, messages.INFO, 'Акаунт оновлено')

                return redirect('home')
        else:
            form = EditUserForm(initial={'first_name': user.first_name,
                                         'last_name': user.last_name,
                                         'username': user.username,
                                         'email': user.email,
                                         })

            form_profile = ProfileForm(initial={
                'phone_number': profile.phone_number,
                'mail_address': profile.mail_address
            })

        context = {
            'title': 'Оновлення інформації',
            'form': form,
            'form_profile': form_profile
        }
        return render(request, 'user_module/edit_account.html', context)

    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого користувача не існує</h2>")


def delete_order(request, id):
    if not request.user.is_authenticated:
        return redirect('home')

    try:
        order = Order.objects.get(id=id)

        if order.user != request.user:
            return redirect('account')

        items = OrderItems.objects.filter(order=id)
        for i in range(items.count()):
            product = Product.objects.get(id=items[i].product.id)
            product.number += items[i].quantity
            product.save()

        Order.objects.get(id=items[0].order.id).delete()

        return redirect('account')
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Такого замовлення не існує</h2>")