from django.urls import path
from .views import product_detail, products_view, add_product, add_category, \
    categories_view, delete_category, delete_product, edit_product
urlpatterns = [
    path('', products_view, name='products'),

    path('products/<int:id>/', product_detail, name='product_detail'),
    path('products/<int:id>/delete', delete_product, name='delete_product'),
    path('products/<int:id>/edit', edit_product, name='edit_product'),
    path('products/add/', add_product, name='add_product'),

    path('categories/', categories_view, name='categories'),
    path('categories/<int:id>/delete/', delete_category, name='delete_category'),
    path('categories/add/', add_category, name='add_category'),
]