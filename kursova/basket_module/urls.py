from django.urls import path
from . import views

urlpatterns = [
    path('basket', views.basket, name='basket'),
    path('add_item_basket/<int:pk>/', views.add_item_basket),
    path('add_item_basket/<int:pk>/product', views.add_item_basket_product),
    path('basket/item/<int:pk>/delete/', views.delete_item_basket),

    path('basket/create_order', views.create_order),

    path('basket/item/<int:pk>/remove_quantity/', views.remove_quantity),
    path('basket/item/<int:pk>/add_quantity/', views.add_quantity),
]