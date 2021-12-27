from django.db import models


class Product(models.Model):
    name = models.CharField('Назва товару', max_length=100)
    image = models.ImageField(upload_to="photo/%Y/%m/%d/")  # записує картрнку в католог
    price = models.CharField('Ціна', max_length=4)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:  # змінюємо назву таблиці для адміна
        verbose_name = 'Тавару'
        verbose_name_plural = 'Товари'