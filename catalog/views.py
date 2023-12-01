# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from catalog.models import Product, Contacts


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
    success_url = reverse_lazy('catalog:product_list')


class ContactsListView(ListView):
    model = Contacts


# def home(request):
#     product_list = Product.objects.all()[:6]
#     context = {
#         'product_list': product_list,
#         'title': 'Shop_Name',
#     }
#     return render(request, 'catalog/home.html', context)

# def product(request, pk):
#     product_info = Product.objects.get(id=pk)
#     context = {
#         'product_info': product_info,
#         'title': 'Product',
#     }
#     return render(request, 'catalog/product_detail.html', context)

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('email')
#         user_message = request.POST.get('message')
#         print(f'{name}: {user_message}')
#     context = {
#         'title': 'Contacts',
#     }
#     return render(request, 'catalog/contacts_list.html', context)
