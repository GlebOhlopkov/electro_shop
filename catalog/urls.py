from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsListView, ProductUpdateView, ProductCreateView

app_name = 'catalog'
urlpatterns = [
    # path('', home, name='home'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('contacts/', ContactsListView.as_view(), name='contacts_list'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
]
