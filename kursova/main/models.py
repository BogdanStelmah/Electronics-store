from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^(\+?(38))?[-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message="Номер телефону повинен бути в форматі '+380XXXXXXXXX'")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, null=True, blank=True)
    mail_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіль'


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
    price = models.FloatField('Ціна')
    discount = models.IntegerField('Знижка', max_length=3)
    discounted_price = models.FloatField('Ціна зі знижкою', max_length=20, default=0)
    number = models.IntegerField('Кількість', max_length=10)
    categories = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:  # змінюємо назву таблиці для адміна
        verbose_name = 'Тавар'
        verbose_name_plural = 'Товари'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, max_length=5)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзина'


class ReviewsProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviews = models.TextField('Відгук', max_length=200)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.BooleanField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderItems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, max_length=5)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Замовленні товари'
        verbose_name_plural = 'Замовленні товари'
