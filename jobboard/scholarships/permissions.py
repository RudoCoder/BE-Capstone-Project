from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrgOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ("organization", "admin")

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (obj.posted_by_id == request.user.id or request.user.role == "admin")
