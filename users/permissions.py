from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Разрешение: пользователь может редактировать только свой профиль
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
