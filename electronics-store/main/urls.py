from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<int:pk>/', views.product, name='product'),
    path('product/<int:pk>/reviews/<int:pk_review>', views.delete_reviews),
]