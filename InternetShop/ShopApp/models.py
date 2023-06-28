from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(verbose_name='Цена', null=False, blank=False, decimal_places=2, max_digits=10)
    image = models.URLField()

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
         db_table = "Products"
         verbose_name = "Продукт"
         verbose_name_plural = "Продукт"