from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('create_product', views.create_product, name='create_product')
]