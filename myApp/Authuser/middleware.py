from django.http import JsonResponse
from django.urls import resolve
from rest_framework_simplejwt.authentication import JWTAuthentication

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authenticator = JWTAuthentication()

    def __call__(self, request):
        try:
            user_auth_tuple = self.jwt_authenticator.authenticate(request)
            if user_auth_tuple:
                request.user, _ = user_auth_tuple
        except Exception:
            pass  # Token invalid or missing — let DRF handle it later

        if not hasattr(request, "user") or not request.user.is_authenticated:
            return self.get_response(request)  # Skip role checks for unauthenticated users

        user = request.user
        url_name = resolve(request.path).url_name

        # Super Admin
        if user.is_super_admin == 1 and user.is_admin == 1:
            return self.get_response(request)

        # Salesperson
        if user.is_super_admin == 0 and user.is_admin == 0:
            if url_name in ['user-listing', 'user-update', 'list-user','delete-user']:
                return JsonResponse({'detail': 'Salesperson access denied'}, status=403)

        return self.get_response(request)
