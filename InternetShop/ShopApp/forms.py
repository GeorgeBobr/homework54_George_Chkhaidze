from django import forms
from django.forms import widgets

class CategoryForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=2000, required=True, label='Описание')
class ProductForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    category = forms.ChoiceField(required=True, label="Категория")
    price = forms.CharField(required=True, label="Цена")
    image = forms.URLField(required=True, label="Картинка")