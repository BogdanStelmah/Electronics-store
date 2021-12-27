# Generated by Django 4.0 on 2021-12-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва товару')),
                ('image', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('price', models.CharField(max_length=4, verbose_name='Ціна')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Тавару',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]