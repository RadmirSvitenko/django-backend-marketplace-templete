from django.db import models
class Subcategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    image = models.ImageField(upload_to='media/images/subcategory/%Y/%m/%d', blank=True, null=True)
    parent = models.ForeignKey(
        'self',  # Указывает на эту же модель
        on_delete=models.SET_NULL,  # Если родитель удаляется, оставить значение пустым
        related_name='children',  # Связь для доступа к дочерним подкатегориям
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

class Category(models.Model):
    subcategory = models.ManyToManyField(Subcategory, related_name='categories')
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    image = models.ImageField(upload_to='media/images/category/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name