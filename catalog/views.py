# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from catalog.forms import ProductForm, VersionForm, ProductModerForm, ProductCreateForm
from catalog.models import Product, Contacts, Version


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    permission_required = 'catalog.view_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'


class ProductModerUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductModerForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = '/users/login'


def get_context_data(self, **kwargs):
    context_data = super().get_context_data(**kwargs)
    VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    if self.request.method == 'POST':
        context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
    else:
        context_data['formset'] = VersionFormset(instance=self.object)
    return context_data


def form_valid(self, form):
    formset = self.get_context_data()['formset']
    self.object = form.save()
    if formset.is_valid():
        formset.instance = self.object
        formset.save()
    return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = '/users/login'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.created_by != self.request.user:
            return Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = '/users/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        return super().form_valid(form)


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
