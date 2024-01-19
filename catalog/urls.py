from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ContactsListView, ProductUpdateView, ProductCreateView, \
    ProductModerUpdateView, CategoryListView

app_name = 'catalog'
urlpatterns = [
    # path('', home, name='home'),
    path('', ProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('product_moder_update/<int:pk>/', ProductModerUpdateView.as_view(), name='product_moder_update'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('contacts/', ContactsListView.as_view(), name='contacts_list'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
]
