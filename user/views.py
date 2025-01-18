from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from cart.models import Cart
from cart.serializers import CartSerializer
from user.models import User
from user.serializers import UserRegisterSerializer, UserLoginSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    @extend_schema(
        summary="Регистрация пользователя",
        description="Создаёт нового пользователя.",
        request=UserRegisterSerializer,
        responses={
            201: {
                "message": "User created successfully!",
                "user": {
                    "id": 1,
                    "email": "user@example.com",
                    "username": "user123"
                }
            }
        }
    )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            # Создание корзины для нового пользователя
            cart = Cart.objects.create(user=user)

            cart_serializer = CartSerializer(cart)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"message": "User created successfully!",
                 "user": serializer.data,
                 "cart": cart_serializer.data
                 },
                status=status.HTTP_201_CREATED,
                headers=headers
            )

class UserLoginViewSet(APIView):
    serializer_class = UserLoginSerializer

    @extend_schema(
        summary="Авторизация пользователя",
        description="Возвращает токены (access и refresh) и профиль пользователя.",
        request=UserLoginSerializer,
        responses={
            200: {
                "message": "Logged in successfully!",
                "refresh_token": "sample_refresh_token",
                "access_token": "sample_access_token",
                "profile": {
                    "email": "user@example.com",
                    "username": "user123",
                    "avatar": "http://example.com/media/default-avatar.png"
                }
            }
        }
    )

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Генерация токенов для пользователя
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        # Получаем корзину пользователя, или создаём если её не существует
        cart, created = Cart.objects.get_or_create(user=user)

        return Response({
            'message': 'Logged in successfully!',
            'refresh_token': str(refresh),
            'access_token': str(access),
            'profile': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'avatar': user.avatar.url if user.avatar else None,
                'cart': CartSerializer(cart).data,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            }
        })
