from .models import Buyer, StaffProfile


def user_role(request):
    """Inject is_maker, is_buyer, and buyer_nav_brands into every template context."""
    if not request.user.is_authenticated:
        return {'is_maker': False, 'is_buyer': False, 'buyer_nav_brands': []}

    is_maker = False
    is_buyer = False
    buyer_nav_brands = []

    if not request.user.is_superuser:
        is_maker = StaffProfile.objects.filter(user=request.user).exists()
        if not is_maker:
            try:
                buyer = Buyer.objects.get(user=request.user)
                is_buyer = True
                buyer_nav_brands = list(buyer.brand.all())
            except Buyer.DoesNotExist:
                pass

    return {'is_maker': is_maker, 'is_buyer': is_buyer, 'buyer_nav_brands': buyer_nav_brands}
