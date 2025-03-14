from django.contrib import admin
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'avatar', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']

