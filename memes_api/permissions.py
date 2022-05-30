from rest_framework import permissions

class OwnerOrReadOnly(permissions.BasePermission):
    '''Read for anyone. Requires user to be loged-in and the owner of the object to update it'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CreateOrReadOnly(permissions.BasePermission):
    '''Read for anyone. Requires user to be loged-in create objects'''
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated


class OwnerLogin(permissions.BasePermission):
    '''Very strict authentication, requires user to be loged-in and the owner of the object to read and update it'''
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class CreateLogin(permissions.BasePermission):
    '''Very strict authentication, requires user to be loged-in read and create objects'''
    def has_permission(self, request, view):
        return request.user.is_authenticated

