from catalog.models import Category
from django.core.cache import cache
from config.settings import CACHE_ENABLED


def get_all_categories():
    if CACHE_ENABLED:
        key = 'queryset'
        queryset = cache.get(key)
        if queryset is None:
            queryset = Category.objects.all()
            cache.set(key, queryset)
    else:
        queryset = Category.objects.all()
    return queryset
