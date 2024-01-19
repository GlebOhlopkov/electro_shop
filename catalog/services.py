from catalog.models import Category


def get_all_categories():
    category_list = Category.objects.all()
    return category_list
