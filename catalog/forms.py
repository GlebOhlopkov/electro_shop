from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['product_name']
        for word in banned_words:
            if word in cleaned_data:
                raise forms.ValidationError('You used blocked word in name')
        return cleaned_data

    def clean_product_description(self):
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['product_description']
        for word in banned_words:
            if word in cleaned_data:
                raise forms.ValidationError('You used blocked word in description')
        return cleaned_data
