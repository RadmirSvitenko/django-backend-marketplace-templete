from rest_framework import serializers
from category.models import Category, Subcategory
from .models import ProductImage, Product, ProductClass

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = ['id', 'title', 'slug', 'image']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subcategories = serializers.PrimaryKeyRelatedField(many=True, queryset=Subcategory.objects.all())
    images = ProductImageSerializer(many=True, read_only=True)
    product_class = ProductClassSerializer()
    price_with_discount = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_price_with_discount(self, obj):
        return obj.price_with_discount

