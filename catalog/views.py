from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        user_message = request.POST.get('message')
        print(f'{name}: {user_message}')
    return render(request, 'catalog/contacts.html')
