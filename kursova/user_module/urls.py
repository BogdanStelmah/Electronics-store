from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),

    path('account', views.account, name='account'),
    path('account/edit/<int:id>/', views.edit_account),
]