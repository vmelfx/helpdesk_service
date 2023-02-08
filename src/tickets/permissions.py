from rest_framework.permissions import BasePermission
from users.schemas import Role


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER

    def has_object_permission(self, request, view, obj):
        if obj.customer == request.user:
            return True
        return False


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER

    def has_object_permission(self, request, view, obj):
        if obj.manager == request.user:
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
