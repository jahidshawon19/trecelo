from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Buyer, Sample, StaffProfile
from .forms import BuyerForm, SampleForm, StaffForm


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
        messages.success(request, f'Sample "{sample.product_name}" updated successfully.')
        return redirect('sample_detail', pk=sample.pk)
    return render(request, 'form.html', {'form': form, 'title': 'Edit Sample'})


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
