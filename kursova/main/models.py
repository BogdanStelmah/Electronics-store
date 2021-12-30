from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Назва категорії', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'


class Product(models.Model):
    name = models.CharField('Назва товару', max_length=100)
    image = models.ImageField(upload_to="photo/%Y/%m/%d/", null=True, blank=True)  # записує картрнку в католог
    description = models.TextField('Опис продукту', null=True)
    price = models.CharField('Ціна', max_length=10)
    discount = models.CharField('Знижка', max_length=3)
    number = models.CharField('Кількість', max_length=10)
    categories = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:  # змінюємо назву таблиці для адміна
        verbose_name = 'Тавар'
        verbose_name_plural = 'Товари'

