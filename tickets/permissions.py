from rest_framework import permissions

class TicketPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'OPTIONS','HEAD']:
            return request.user.has_perm("tickets.view_ticket")
          
        if request.method in ("POST"):
            return request.user.has_perm("tickets.add_ticket")
          
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("tickets.change_ticket")

        if request.method == "DELETE":
            return request.user.has_perm("tickets.delete_ticket")

        return False