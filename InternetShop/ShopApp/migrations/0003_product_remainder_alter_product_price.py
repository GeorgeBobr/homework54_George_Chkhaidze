# Generated by Django 4.2.2 on 2023-07-03 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_alter_product_price_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remainder',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
    ]