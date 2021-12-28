from django.urls import path
from . import views

urlpatterns = [
    path('create_product', views.create_product, name='create_product'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('admin_panel/users', views.users_db, name='users_db'),
    path('admin_panel/users/delete/<int:id>/', views.delete_user),
    path('admin_panel/users/edit/<int:id>/', views.edit_user)
]