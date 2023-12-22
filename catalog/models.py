from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='category_name')
    category_description = models.TextField(verbose_name='category_description')
    #created_at = models.DateTimeField(**NULLABLE, verbose_name='created_at')

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


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, **NULLABLE, verbose_name='product')
    version_number = models.IntegerField(default=1, verbose_name='version_number')
    version_name = models.CharField(max_length=50, verbose_name='version_name')
    is_active = models.BooleanField(default=True, verbose_name='is_active')

    def __str__(self):
        return f'{self.version_number}: {self.version_name} ({self.product})'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'


class Contacts(models.Model):
    phone = models.CharField(max_length=30, verbose_name='phone')
    email = models.CharField(max_length=100, verbose_name='email')

    def __str__(self):
        return f'phone: {self.phone}, email: {self.email}'

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
