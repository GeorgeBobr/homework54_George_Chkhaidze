# Generated by Django 4.2.2 on 2023-06-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]
