from django.urls import path
from .views import product_view, products_view, product_add_view, category_add_view, category_edit_view, \
    categories_view, delete_category, delete_product, product_edit_view
urlpatterns = [
    path('', products_view, name='products_view'),
    path('products', products_view, name='products_view'),
    path('products/<int:id>/', product_view, name='product_view'),
    path('products/<int:id>/delete', delete_product, name='delete_product'),
    path('products/<int:id>/edit', product_edit_view, name='product_edit_view'),
    path('categories/add/', category_add_view, name='category_add_view'),
    path('products/add/', product_add_view, name='product_add_view'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:id>/delete/', delete_category, name='delete_category'),
    path('categories/<int:id>/edit/', category_edit_view, name='category_edit_view')

]