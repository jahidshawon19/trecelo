from django.shortcuts import redirect
from django.contrib import messages


class ReadOnlyRolesMiddleware:
    """
    Block every POST request from a Top Management or General Customer user.
    Both roles have full view access but cannot create, edit, or delete anything.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.method == 'POST'
            and request.user.is_authenticated
            and not request.user.is_staff
            and not request.user.is_superuser
        ):
            try:
                from .models import GeneralCustomer, TopManagement
                is_readonly = (
                    TopManagement.objects.filter(user=request.user).exists()
                    or GeneralCustomer.objects.filter(user=request.user).exists()
                )
                if is_readonly:
                    messages.error(request, 'You have view-only access and cannot make changes.')
                    referer = request.META.get('HTTP_REFERER', '')
                    return redirect(referer or 'dashboard')
            except Exception:
                pass  # never block a request due to a middleware error

        return self.get_response(request)


# Keep the old name as an alias so existing settings.py entries still work
TopManagementReadOnlyMiddleware = ReadOnlyRolesMiddleware
