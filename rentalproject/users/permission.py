from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allow read only if authenticated.
    Allow write only for admin users.
    """
    
    def has_permission(self, request, view):
       #Require authentication for all requests (including GET)
       if request.user or not request.user.is_authenticated:
            return False
        
       #for read-only methods, allow  my authenticated users
       if request.method in SAFE_METHODS:
            return True
       
       #for unsafe methids, only allow admin users
       return bool(request.user.is_superuser or getattr(request.user, 'role', None) == 'admin')