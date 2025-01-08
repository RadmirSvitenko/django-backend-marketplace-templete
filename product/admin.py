from django.contrib import admin
from .forms import ProductForm
from .models import Product, ProductImage, ProductClass

class ProductImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 5

@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
    list_filter = ['id', 'title', 'image']
    search_fields = ['title']
    list_editable = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'slug']
    list_editable = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = [
        'id',
        'title',
        'slug',
        'description',
        'price',
        'discount',
        'price_with_discount',
        'product_class',
        'in_stock',
        'created_at',
        'updated_at',
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'subcategories', 'title', 'slug',  'price', 'discount', 'product_class', 'in_stock']
    search_fields = ['category', 'subcategories', 'title', 'slug',  'price', 'discount', 'product_class', 'in_stock']
    list_editable = ['title', 'price', 'discount', 'in_stock', 'product_class']
    inlines = [ProductImageInline]



