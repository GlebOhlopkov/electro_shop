from django import template

register = template.Library()


@register.filter()
def photo_path(photo_product):
    if photo_product:
        return f'/media/{photo_product}'
    return f'#'


@register.simple_tag()
def image_path(photo_product):
    if photo_product:
        return f'/media/{photo_product}'
    return f'#'
