from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),

    path('account', views.account, name='account'),
    path('account/edit/<int:id>/', views.edit_account),

    path('order/<int:id>/delete/', views.delete_order),

]
