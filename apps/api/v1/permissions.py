import logging

from rest_framework.permissions import BasePermission, SAFE_METHODS


logger = logging.getLogger(__name__)


class IsAuthorOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        logging.info("Call permissions")
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        logging.info("Call object permissions")
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or request.user.is_staff
        )
