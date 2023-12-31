# Generated by Django 4.2.2 on 2023-06-27 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('image', models.URLField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='Products', to='ShopApp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукт',
                'db_table': 'Products',
            },
        ),
    ]
