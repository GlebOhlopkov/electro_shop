from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()[:6]
    context = {
        'product_list': product_list,
        'title': 'Shop_Name',
    }
    return render(request, 'catalog/home.html', context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': 'Product',
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        user_message = request.POST.get('message')
        print(f'{name}: {user_message}')
    context = {
        'title': 'Contacts',
    }
    return render(request, 'catalog/contacts.html', context)
