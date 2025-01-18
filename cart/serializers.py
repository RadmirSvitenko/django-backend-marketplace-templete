from .models import Cart, CartItem
from user.models import User
from rest_framework import serializers
from product.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField(default=1, required=False)
    class Meta:
        model = CartItem
        fields = '__all__'
        ordering = ['id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id', None)
        product_id = validated_data.pop('product_id', None)
        quantity = validated_data.pop('quantity', 1)

        # Получаем корзину пользователя
        if user_id and product_id:
            user = User.objects.get(id=user_id)
            cart, created = Cart.objects.get_or_create(user=user)

            # Добавляем продукт в корзину
            cart_item = CartItem.objects.create(cart=cart, product_id=product_id, quantity=quantity)
            return CartItemSerializer(cart_item).data

        raise serializers.ValidationError("User ID and Product ID are required.")


class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'