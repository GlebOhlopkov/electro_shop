from django.db import models


class Product(models.Model):
    attr1 = models.CharField(max_length=100, verbose_name='attr1')
    attr2 = models.CharField(max_length=100, verbose_name='attr2')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Category(models.Model):
    attr1 = models.CharField(max_length=100, verbose_name='attr1')
    attr2 = models.CharField(max_length=100, verbose_name='attr2')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

