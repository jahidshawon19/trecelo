from .models import Buyer, GeneralCustomer, StaffProfile, TopManagement


def user_role(request):
    """Inject role flags and buyer_nav_brands into every template context."""
    if not request.user.is_authenticated:
        return {
            'is_maker':            False,
            'is_buyer':            False,
            'is_top_management':   False,
            'is_general_customer': False,
            'buyer_nav_brands':    [],
        }

    is_maker            = False
    is_buyer            = False
    is_top_management   = False
    is_general_customer = False
    buyer_nav_brands    = []

    if not request.user.is_superuser:
        is_maker = StaffProfile.objects.filter(user=request.user).exists()
        if not is_maker:
            try:
                buyer = Buyer.objects.get(user=request.user)
                is_buyer         = True
                buyer_nav_brands = list(buyer.brand.all())
            except Buyer.DoesNotExist:
                try:
                    is_top_management = TopManagement.objects.filter(user=request.user).exists()
                    if not is_top_management:
                        is_general_customer = GeneralCustomer.objects.filter(user=request.user).exists()
                except Exception:
                    pass

    return {
        'is_maker':            is_maker,
        'is_buyer':            is_buyer,
        'is_top_management':   is_top_management,
        'is_general_customer': is_general_customer,
        'buyer_nav_brands':    buyer_nav_brands,
    }
