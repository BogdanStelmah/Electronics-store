from django.contrib import admin
from .models import Product, ProductCategory, Basket, ReviewsProduct, Profile, Order, OrderItems

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(ReviewsProduct)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItems)