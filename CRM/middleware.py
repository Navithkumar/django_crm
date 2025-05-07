from django.http import JsonResponse
from django.urls import resolve

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if not user.is_authenticated:
            return self.get_response(request)

        # Get current endpoint's name (e.g., "user-list", "client-detail")
        resolver_match = resolve(request.path)
        current_url_name = resolver_match.url_name

        # Role: Super Admin
        if user.is_super_admin == 1 and user.is_admin == 1:
            return self.get_response(request)  # full access

        # Role: Salesperson
        if user.is_super_admin == 0 and user.is_admin == 0:
            blocked_for_sales = ['delete-user', 'list-user', 'user-update','user-listing']
            if current_url_name in blocked_for_sales:
                return JsonResponse({'detail': 'Salesperson access denied for this resource.'}, status=403)

        return self.get_response(request)
