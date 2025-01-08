from django.db import models
from django.db.models import ManyToManyField

from category.models import Category, Subcategory

class ProductClass(models.Model):
    title = models.CharField('Класс продукта', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='slug', max_length=100, unique=True)
    image = models.ImageField('images_product_class', upload_to='media/images/product/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = "Класс продукта"
        verbose_name_plural = "Классы продуктов"
        ordering = ['title']

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    title = models.CharField('Название изображения продукта', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='slug', max_length=100, unique=True)
    image = models.ImageField('image', upload_to='media/images/product/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, verbose_name="Категория продукта", on_delete=models.SET_NULL, null=True, related_name='products', blank=True)
    subcategories = models.ManyToManyField(Subcategory, verbose_name="Подкатегории продукта", blank=True, related_name='products')
    title = models.CharField(verbose_name='Название', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='slug', max_length=100, unique=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True, max_length=255)
    price = models.DecimalField(verbose_name='Цена', max_digits=7, decimal_places=2)
    discount = models.DecimalField(verbose_name='Скидка (%)', max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    images = ManyToManyField(ProductImage, verbose_name='Изображения продукта', related_name='products')
    product_class = models.ForeignKey(ProductClass, verbose_name='Класс продукта', on_delete=models.SET_NULL, null=True, blank=True, related_name='products', default=1)
    in_stock = models.BooleanField('в наличии', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['id']

    def __str__(self):
        return self.title

    @property
    def price_with_discount(self):
        if self.discount and self.price:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price



