from django.db import models
from product.models import Product
from user.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзины пользователей'

    def __str__(self):
        return f"cart: {self.user.email}"

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Элемент корзины пользователя'
        verbose_name_plural = 'Элементы корзины пользователей'

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in {self.cart.user.email}s cart"

    @property
    def total_price(self):
        return self.quantity * self.product.price