from rest_framework import permissions


class CatalogPermissionClass(permissions.BasePermission):

  def has_permission(self, request, view):
      #logica da permissao
      
      return True
 