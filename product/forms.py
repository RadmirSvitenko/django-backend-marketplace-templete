from django import forms
from .models import Product, ProductClass

class ProductForm(forms.ModelForm):
    product_class = forms.ModelChoiceField(queryset=ProductClass.objects.all(), required=False, initial=ProductClass.objects.get(id=1))
    class Meta:
        model = Product
        fields = '__all__'

    # Устанавливаем значение по умолчанию для product_class в одну строку
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_class'].initial = ProductClass.objects.get(id=1)