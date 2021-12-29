from django.urls import path
from . import views

urlpatterns = [
    path('create_product', views.create_product, name='create_product'),
    path('admin_panel', views.admin_panel, name='admin_panel'),

    path('admin_panel/users', views.users_db, name='users_db'),
    path('admin_panel/users/delete/<int:id>/', views.delete_user),
    path('admin_panel/users/edit/<int:id>/', views.edit_user),

    path('admin_panel/category', views.category_db, name='category_db'),
    path('admin_panel/category/add', views.add_category, name='add_category'),
    path('admin_panel/category/delete/<int:id>/', views.delete_user),
    path('admin_panel/category/edit/<int:id>/', views.delete_user),

    path('admin_panel/product', views.product_db, name='product_db'),
    path('admin_panel/product/add', views.add_product, name='add_product'),
    path('admin_panel/product/delete/<int:id>/', views.delete_user),
    path('admin_panel/product/edit/<int:id>/', views.delete_user),

]