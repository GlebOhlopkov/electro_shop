import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        # clear all tables in DB
        Category.objects.all().delete()
        Product.objects.all().delete()

        # fill table category from json-file
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            catalog_data = json.load(file)
            for data in catalog_data:
                if data['model'] == 'catalog.category':
                    Category.objects.create(category_name=data['fields']['category_name'],
                                            category_description=data['fields']['category_description'])

        # fill table product from json-file
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            catalog_data = json.load(file)
            for data in catalog_data:
                if data['model'] == 'catalog.product':
                    Product.objects.create(product_name=data['fields']['product_name'],
                                           product_description=data['fields']['product_description'],
                                           product_image=data['fields']['product_image'],
                                           product_category=Category.objects.get(id=data['fields']['product_category']),
                                           product_price=data['fields']['product_price'],
                                           product_datetime_create=data['fields']['product_datetime_create'],
                                           product_datetime_change=data['fields']['product_datetime_change'])
