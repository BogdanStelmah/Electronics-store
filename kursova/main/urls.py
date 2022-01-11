from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<int:pk>/', views.product, name='product'),
]