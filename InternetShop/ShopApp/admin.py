from django.contrib import admin
from ShopApp.models import Product, Category

admin.site.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['price']
    search_fields = ['title', 'description']
    fields = ['title', 'price', 'content', 'created_at', 'category']
    readonly_fields = ['created_at']


admin.site.register(Product, ProductAdmin)