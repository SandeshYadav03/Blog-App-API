from rest_framework import permissions

class IsOwner(permissions.BasePermission):      
      """Object level permission"""
      def has_object_permission(self, request, view, obj):
        """ SAFE METHOD: GET, POST """
        if request.method in permissions.SAFE_METHODS:
            return True

        """ PUT/PATCH, DELETE """
        if obj.owner is not None:
          return obj.owner_id == request.user.id
        return False