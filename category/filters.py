import django_filters
from .models import Category, Subcategory
class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']
class SubcategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Subcategory
        fields = ['name']