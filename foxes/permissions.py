from rest_framework.permissions import BasePermission


class IsAFox(BasePermission):
    """
    Is the current user a fox?
    """
    def has_permission(self, request, view):
        return getattr(request.user, 'fox', None) is not None
