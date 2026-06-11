from .models import Buyer, StaffProfile


def user_role(request):
    """Inject is_maker and is_buyer flags into every template context."""
    if not request.user.is_authenticated:
        return {'is_maker': False, 'is_buyer': False}

    is_maker = False
    is_buyer = False

    if not request.user.is_superuser:
        is_maker = StaffProfile.objects.filter(user=request.user).exists()
        if not is_maker:
            is_buyer = Buyer.objects.filter(user=request.user).exists()

    return {'is_maker': is_maker, 'is_buyer': is_buyer}
