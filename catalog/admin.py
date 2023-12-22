from django.contrib import admin

from catalog.models import Product, Category, Contacts, Version


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_category',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_active',)
    list_filter = ('product',)


@admin.register(Contacts)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
