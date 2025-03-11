from .models import Category, Subcategory
from rest_framework import serializers
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subcategory = serializers.PrimaryKeyRelatedField(many=True, queryset=Subcategory.objects.all())
    class Meta:
        model = Category
        fields = '__all__'