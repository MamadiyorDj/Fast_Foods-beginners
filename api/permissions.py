from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.models import Orders

class IsUserInSuperuser(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user.is_superuser):
            return view
        else:
            return False
    # def has_object_permission(self, request, view, obj):
    #     if bool(request.user.is_superuser) and (request.method in SAFE_METHODS):
    #         return obj



class IsUserInOfitsiant(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user.is_superuser) or request.user.user_role == "O":
            return view
        else:
            return False

class IsUserInUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False


