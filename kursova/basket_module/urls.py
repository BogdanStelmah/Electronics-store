from django.urls import path
from . import views

urlpatterns = [
    path('basket', views.basket, name='basket'),
    path('add_item_basket/<int:pk>/', views.add_item_basket),
    path('basket/item/<int:pk>/delete/', views.delete_item_basket)
]