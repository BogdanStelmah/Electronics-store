from django.contrib import messages

from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductForm


# @login_required(login_url='login')
def index(request):
    product = Product.objects.order_by('-name')  # сортує по імені, all() виводить всі записи (- це ревьорс) ([:1] - виводить 1 запис)
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'product': product})


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


def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('home')
    else:
        context = {
            'title': 'Адмін панель'
        }
        return render(request, 'main/admin_panel.html', context)
