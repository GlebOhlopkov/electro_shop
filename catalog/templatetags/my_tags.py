from django import template

register = template.Library()


@register.filter()
def mymedia(photo_product):
    if photo_product:
        return f'/media/product/{photo_product}'
    return f'#'
