# Generated by Django 4.0 on 2021-12-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Тавар', 'verbose_name_plural': 'Товари'},
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.productcategory'),
        ),
    ]