from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='category_name')
    category_description = models.TextField(verbose_name='category_description')
    created_at = models.DateTimeField(**NULLABLE, verbose_name='created_at')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='product_name')
    product_description = models.TextField(verbose_name='product_description')
    product_image = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='product_image')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='product_category')
    product_price = models.IntegerField(verbose_name='product_price')
    product_datetime_create = models.DateTimeField(**NULLABLE, verbose_name='product_datetime_create')
    product_datetime_change = models.DateTimeField(**NULLABLE, verbose_name='product_datetime_change')

    def __str__(self):
        return f'{self.product_name} ({self.product_category}, {self.product_price})'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
