from rest_framework import permissions

class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='moderators').exists()

class IsOwnerOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, 'owner') and obj.owner == request.user:
            return True
        if request.user and request.user.is_authenticated and request.user.groups.filter(name='moderators').exists():
            if request.method in ('PUT','PATCH'):
                return True
        return False
