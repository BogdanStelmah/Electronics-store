from django.contrib import admin
from .models import Product, ProductCategory, Basket, ReviewsProduct

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(ReviewsProduct)