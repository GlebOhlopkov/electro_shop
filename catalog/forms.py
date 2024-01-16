from django import forms
from django.forms import CheckboxInput, Select

from catalog.models import Product, Version

BANNED_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)


class BootstrapFormStyleMixin:
    fields: dict

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_bootstrap_classes()

    def _add_bootstrap_classes(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductCreateForm(BootstrapFormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        self._validate_for_banned_words(cleaned_data, 'You used blocked word in name')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        self._validate_for_banned_words(cleaned_data, 'You used blocked word in description')
        return cleaned_data

    @staticmethod
    def _validate_for_banned_words(field, exception_message):
        for word in BANNED_WORDS:
            if word in field:
                raise forms.ValidationError(exception_message)


class ProductModerForm(BootstrapFormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price',
                  'product_is_published')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        self._validate_for_banned_words(cleaned_data, 'You used blocked word in name')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        self._validate_for_banned_words(cleaned_data, 'You used blocked word in description')
        return cleaned_data

    @staticmethod
    def _validate_for_banned_words(field, exception_message):
        for word in BANNED_WORDS:
            if word in field:
                raise forms.ValidationError(exception_message)


class ProductForm(BootstrapFormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_image', 'product_price')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        self._validate_for_banned_words(cleaned_data, 'You used blocked word in name')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        self._validate_for_banned_words(cleaned_data, 'You used blocked word in description')
        return cleaned_data

    @staticmethod
    def _validate_for_banned_words(field, exception_message):
        for word in BANNED_WORDS:
            if word in field:
                raise forms.ValidationError(exception_message)


class VersionForm(BootstrapFormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
