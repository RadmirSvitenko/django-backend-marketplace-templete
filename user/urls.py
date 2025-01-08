from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterViewSet, UserLoginViewSet

router = DefaultRouter()
router.register(r'sign-up', UserRegisterViewSet, basename='sign-up')

urlpatterns = [
    path('', include(router.urls)),
    path('sign-in/', UserLoginViewSet.as_view(), name='sign-in'),
]
