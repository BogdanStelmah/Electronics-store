from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_product', views.create_product, name='create_product'),
    path('admin_panel', views.admin_panel, name='admin_panel')
]