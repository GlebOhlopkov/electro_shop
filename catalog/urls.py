from django.urls import path
from catalog.views import home, contacts, product

app_name = 'catalog'
urlpatterns = [
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
]
