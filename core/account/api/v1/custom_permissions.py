from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsNotAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return request.user.is_anonymous