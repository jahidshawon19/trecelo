from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Buyer, Product, StaffProfile
from .forms import BuyerForm, ProductForm, StaffForm


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
            return redirect('product_list')
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


# ---------- PRODUCT CRUD ----------
@login_required
def product_list(request):
    if request.user.is_staff or request.user.is_superuser:
        products = Product.objects.select_related('buyer', 'maker__user').all()
    else:
        try:
            buyer = Buyer.objects.get(user=request.user)
            products = Product.objects.select_related('buyer', 'maker__user').filter(buyer=buyer)
        except Buyer.DoesNotExist:
            products = Product.objects.none()
    return render(request, 'product_list.html', {'products': products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related('buyer', 'maker__user'), pk=pk)
    if not (request.user.is_staff or request.user.is_superuser):
        try:
            buyer = Buyer.objects.get(user=request.user)
            if product.buyer != buyer:
                messages.error(request, 'You do not have permission to view that product.')
                return redirect('product_list')
        except Buyer.DoesNotExist:
            return redirect('product_list')
    return render(request, 'product_detail.html', {'product': product})


@login_required
@user_passes_test(is_staff_or_admin)
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save()
        messages.success(request, f'Product "{product.product_name}" created successfully.')
        return redirect('product_detail', pk=product.pk)
    return render(request, 'form.html', {'form': form, 'title': 'Add Product'})


@login_required
@user_passes_test(is_staff_or_admin)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, f'Product "{product.product_name}" updated successfully.')
        return redirect('product_detail', pk=product.pk)
    return render(request, 'form.html', {'form': form, 'title': 'Edit Product'})


@login_required
@user_passes_test(is_staff_or_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name = product.product_name
        product.delete()
        messages.success(request, f'Product "{name}" deleted successfully.')
        return redirect('product_list')
    return render(request, 'confirm_delete.html', {'object': product})
