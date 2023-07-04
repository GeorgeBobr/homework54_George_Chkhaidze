from django import forms
from ShopApp.models import Category

class CategoryForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=2000, required=True, label='Описание')
class ProductForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, label="Категория")
    remainder = forms.IntegerField(required=True, label="Остаток")
    price = forms.CharField(required=True, label="Цена$")
    image = forms.URLField(required=True, label="Картинка")