from django.shortcuts import render

from catalog.models import Product


def home(request):
    print(Product.objects.order_by('-product_datetime_change').all()[:5])
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        user_message = request.POST.get('message')
        print(f'{name}: {user_message}')
    return render(request, 'catalog/contacts.html')
