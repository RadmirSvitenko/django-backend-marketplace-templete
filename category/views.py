from rest_framework import viewsets, filters
from .models import Category, Subcategory
from django_filters import rest_framework as dj_filters
from .serializers import CategorySerializer, SubcategorySerializer
from .filters import CategoryFilter, SubcategoryFilter
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(summary="Список категорий"),
    retrieve=extend_schema(summary="Детали категории"),
    create=extend_schema(summary="Создать категорию"),
    update=extend_schema(summary="Обновить категорию"),
    partial_update=extend_schema(summary="Частичное обновление категории"),
    destroy=extend_schema(summary="Удалить категорию"),
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = CategoryFilter
    search_fields = ['name']


@extend_schema_view(
    list=extend_schema(summary="Список подкатегорий"),
    retrieve=extend_schema(summary="Детали подкатегории"),
    create=extend_schema(summary="Создать подкатегорию"),
    update=extend_schema(summary="Обновить подкатегорию"),
    partial_update=extend_schema(summary="Частичное обновление подкатегории"),
    destroy=extend_schema(summary="Удалить подкатегорию"),
)

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = SubcategoryFilter
    search_fields = ['name']