from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True, null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='Описание', blank=True)

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        db_table = "Categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True, null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='Описание')
    category = models.ForeignKey("ShopApp.Category",
                                on_delete=models.RESTRICT,
                                verbose_name="Категория",
                                related_name="Products",
                                null=True)
    remainder = models.IntegerField(verbose_name='Остаток', default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(verbose_name='Цена', null=False, blank=False, max_digits=7, decimal_places=2,
                                validators=[MinValueValidator(0)])
    image = models.URLField(verbose_name="Картинка")

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
         db_table = "Products"
         verbose_name = "Продукт"
         verbose_name_plural = "Продукт"