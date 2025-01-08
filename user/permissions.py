from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Разрешает доступ только авторизованным пользователям для всех методов, кроме GET.
    """

    def has_permission(self, request, view):
        # Разрешить GET-запросы для всех пользователей
        if request.method == 'GET':
            return True

        # Разрешить доступ для аутентификации (например, POST для login/signup)
        if request.method in ['POST', 'OPTIONS', 'HEAD']:
            return True

        # Для всех остальных методов (PUT, PATCH, DELETE) доступ только для авторизованных пользователей
        return request.user and request.user.is_authenticated
