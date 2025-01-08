import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Минимальная цена')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Максимальная цена')
    class Meta:
        model = Product
        fields = ['title', 'category', 'slug', 'subcategories', 'created_at', 'updated_at']