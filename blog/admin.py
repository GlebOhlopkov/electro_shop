from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'text', 'image', 'created_at', 'is_published', 'views_count')
    list_filter = ('created_at', 'views_count',)
    search_fields = ('title', 'text',)
