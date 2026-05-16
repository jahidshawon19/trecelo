from django.contrib import admin
from .models import Buyer, Product, StaffProfile, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['uploaded_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['product_name', 'buyer', 'maker', 'submission_date']
    list_filter = ['buyer', 'maker']
    search_fields = ['product_name']


admin.site.register(Buyer)
admin.site.register(StaffProfile)
