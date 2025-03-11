from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets, filters
from .models import Product
from .filters import ProductFilter
from django_filters import rest_framework as dj_filters
from .serializers import ProductSerializer
from .pagination import CustomProductPagination
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Products'])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomProductPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


