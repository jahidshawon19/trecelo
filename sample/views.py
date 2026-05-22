from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Brand, Buyer, Category, ChallengeImage, ChallengeIn, GG, Sample, StaffProfile
from .forms import BrandForm, BuyerForm, CategoryForm, ChallengeInForm, GGForm, SampleForm, StaffForm


def is_staff_or_admin(user):
    return user.is_staff or user.is_superuser


def is_superadmin(user):
    return user.is_superuser


# ---------- LOGIN ----------
def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user:
            login(request, user)
            return redirect('sample_list')
        return render(request, 'login.html', {'error': 'Invalid username or password. Please try again.'})
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# ---------- STAFF CRUD (SUPERADMIN ONLY) ----------
@login_required
@user_passes_test(is_superadmin)
def staff_list(request):
    staffs = StaffProfile.objects.select_related('user').all()
    return render(request, 'staff_list.html', {'staffs': staffs})


@login_required
@user_passes_test(is_superadmin)
def staff_create(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Staff member created successfully.')
        return redirect('staff_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Staff'})


@login_required
@user_passes_test(is_superadmin)
def staff_update(request, pk):
    staff = get_object_or_404(StaffProfile, pk=pk)
    form = StaffForm(request.POST or None, instance=staff)
    if form.is_valid():
        form.save()
        messages.success(request, f'Staff member "{staff.user.username}" updated successfully.')
        return redirect('staff_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Staff'})


@login_required
@user_passes_test(is_superadmin)
def staff_delete(request, pk):
    staff = get_object_or_404(StaffProfile, pk=pk)
    if request.method == 'POST':
        name = staff.user.username
        staff.user.delete()
        messages.success(request, f'Staff member "{name}" deleted successfully.')
        return redirect('staff_list')
    return render(request, 'confirm_delete.html', {'object': staff})


# ---------- BUYER CRUD ----------
@login_required
@user_passes_test(is_staff_or_admin)
def buyer_list(request):
    buyers = Buyer.objects.select_related('user').all()
    return render(request, 'buyer_list.html', {'buyers': buyers})


@login_required
@user_passes_test(is_staff_or_admin)
def buyer_create(request):
    form = BuyerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Buyer created successfully.')
        return redirect('buyer_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Buyer'})


@login_required
@user_passes_test(is_staff_or_admin)
def buyer_update(request, pk):
    buyer = get_object_or_404(Buyer, pk=pk)
    form = BuyerForm(request.POST or None, instance=buyer)
    if form.is_valid():
        form.save()
        messages.success(request, f'Buyer "{buyer.buyer_name}" updated successfully.')
        return redirect('buyer_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Buyer'})


@login_required
@user_passes_test(is_staff_or_admin)
def buyer_delete(request, pk):
    buyer = get_object_or_404(Buyer, pk=pk)
    if request.method == 'POST':
        name = buyer.buyer_name
        buyer.user.delete()
        messages.success(request, f'Buyer "{name}" deleted successfully.')
        return redirect('buyer_list')
    return render(request, 'confirm_delete.html', {'object': buyer})


# ---------- CATEGORY CRUD ----------
@login_required
@user_passes_test(is_staff_or_admin)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'lookup_list.html', {
        'items': categories,
        'title': 'Categories',
        'create_url': 'category_create',
        'update_url': 'category_update',
        'delete_url': 'category_delete',
        'field': 'name',
    })


@login_required
@user_passes_test(is_staff_or_admin)
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Category created successfully.')
        return redirect('category_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Category'})


@login_required
@user_passes_test(is_staff_or_admin)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(request, f'Category "{category.name}" updated successfully.')
        return redirect('category_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Category'})


@login_required
@user_passes_test(is_staff_or_admin)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f'Category "{name}" deleted successfully.')
        return redirect('category_list')
    return render(request, 'confirm_delete.html', {'object': category})


# ---------- BRAND CRUD ----------
@login_required
@user_passes_test(is_staff_or_admin)
def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'lookup_list.html', {
        'items': brands,
        'title': 'Brands',
        'create_url': 'brand_create',
        'update_url': 'brand_update',
        'delete_url': 'brand_delete',
        'field': 'name',
    })


@login_required
@user_passes_test(is_staff_or_admin)
def brand_create(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Brand created successfully.')
        return redirect('brand_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Brand'})


@login_required
@user_passes_test(is_staff_or_admin)
def brand_update(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    form = BrandForm(request.POST or None, instance=brand)
    if form.is_valid():
        form.save()
        messages.success(request, f'Brand "{brand.name}" updated successfully.')
        return redirect('brand_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Brand'})


@login_required
@user_passes_test(is_staff_or_admin)
def brand_delete(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        name = brand.name
        brand.delete()
        messages.success(request, f'Brand "{name}" deleted successfully.')
        return redirect('brand_list')
    return render(request, 'confirm_delete.html', {'object': brand})


# ---------- GG CRUD ----------
@login_required
@user_passes_test(is_staff_or_admin)
def gg_list(request):
    ggs = GG.objects.all()
    return render(request, 'lookup_list.html', {
        'items': ggs,
        'title': 'GGs',
        'create_url': 'gg_create',
        'update_url': 'gg_update',
        'delete_url': 'gg_delete',
        'field': 'title',
    })


@login_required
@user_passes_test(is_staff_or_admin)
def gg_create(request):
    form = GGForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'GG created successfully.')
        return redirect('gg_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add GG'})


@login_required
@user_passes_test(is_staff_or_admin)
def gg_update(request, pk):
    gg = get_object_or_404(GG, pk=pk)
    form = GGForm(request.POST or None, instance=gg)
    if form.is_valid():
        form.save()
        messages.success(request, f'GG "{gg.title}" updated successfully.')
        return redirect('gg_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit GG'})


@login_required
@user_passes_test(is_staff_or_admin)
def gg_delete(request, pk):
    gg = get_object_or_404(GG, pk=pk)
    if request.method == 'POST':
        title = gg.title
        gg.delete()
        messages.success(request, f'GG "{title}" deleted successfully.')
        return redirect('gg_list')
    return render(request, 'confirm_delete.html', {'object': gg})


# ---------- CHALLENGE IN CRUD ----------
@login_required
@user_passes_test(is_staff_or_admin)
def challengein_list(request):
    challenges = ChallengeIn.objects.all()
    return render(request, 'lookup_list.html', {
        'items': challenges,
        'title': 'Challenges In',
        'create_url': 'challengein_create',
        'update_url': 'challengein_update',
        'delete_url': 'challengein_delete',
        'field': 'title',
    })


@login_required
@user_passes_test(is_staff_or_admin)
def challengein_create(request):
    form = ChallengeInForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Challenge In created successfully.')
        return redirect('challengein_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Challenge In'})


@login_required
@user_passes_test(is_staff_or_admin)
def challengein_update(request, pk):
    challenge = get_object_or_404(ChallengeIn, pk=pk)
    form = ChallengeInForm(request.POST or None, instance=challenge)
    if form.is_valid():
        form.save()
        messages.success(request, f'Challenge In "{challenge.title}" updated successfully.')
        return redirect('challengein_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Challenge In'})


@login_required
@user_passes_test(is_staff_or_admin)
def challengein_delete(request, pk):
    challenge = get_object_or_404(ChallengeIn, pk=pk)
    if request.method == 'POST':
        title = challenge.title
        challenge.delete()
        messages.success(request, f'Challenge In "{title}" deleted successfully.')
        return redirect('challengein_list')
    return render(request, 'confirm_delete.html', {'object': challenge})


# ---------- SAMPLE CRUD ----------
@login_required
def sample_list(request):
    if request.user.is_staff or request.user.is_superuser:
        samples = Sample.objects.select_related('buyer', 'maker__user').all()
    else:
        try:
            buyer = Buyer.objects.get(user=request.user)
            samples = Sample.objects.select_related('buyer', 'maker__user').filter(buyer=buyer)
        except Buyer.DoesNotExist:
            samples = Sample.objects.none()
    return render(request, 'sample_list.html', {'samples': samples})


@login_required
def sample_detail(request, pk):
    sample = get_object_or_404(Sample.objects.select_related('buyer', 'maker__user'), pk=pk)
    if not (request.user.is_staff or request.user.is_superuser):
        try:
            buyer = Buyer.objects.get(user=request.user)
            if sample.buyer != buyer:
                messages.error(request, 'You do not have permission to view that sample.')
                return redirect('sample_list')
        except Buyer.DoesNotExist:
            return redirect('sample_list')
    return render(request, 'sample_detail.html', {'sample': sample})


@login_required
@user_passes_test(is_staff_or_admin)
def sample_create(request):
    form = SampleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        sample = form.save()
        for img in request.FILES.getlist('challenge_images'):
            ChallengeImage.objects.create(sample=sample, image=img)
        messages.success(request, f'Sample "{sample.product_name}" created successfully.')
        return redirect('sample_detail', pk=sample.pk)
    return render(request, 'form.html', {'form': form, 'title': 'Add Sample'})


@login_required
@user_passes_test(is_staff_or_admin)
def sample_update(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    form = SampleForm(request.POST or None, request.FILES or None, instance=sample)
    if form.is_valid():
        form.save()
        # Delete removed challenge images
        for img_id in request.POST.getlist('delete_challenge_images'):
            ChallengeImage.objects.filter(pk=img_id, sample=sample).delete()
        # Add new challenge images
        for img in request.FILES.getlist('challenge_images'):
            ChallengeImage.objects.create(sample=sample, image=img)
        messages.success(request, f'Sample "{sample.product_name}" updated successfully.')
        return redirect('sample_detail', pk=sample.pk)
    challenge_images = sample.challenge_images.all()
    return render(request, 'form.html', {'form': form, 'title': 'Edit Sample', 'challenge_images': challenge_images})


@login_required
@user_passes_test(is_staff_or_admin)
def sample_delete(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    if request.method == 'POST':
        name = sample.product_name
        sample.delete()
        messages.success(request, f'Sample "{name}" deleted successfully.')
        return redirect('sample_list')
    return render(request, 'confirm_delete.html', {'object': sample})
