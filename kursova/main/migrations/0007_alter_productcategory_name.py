# Generated by Django 4.0 on 2022-01-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Назва категорії'),
        ),
    ]