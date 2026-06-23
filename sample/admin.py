from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Brand, Buyer, Category, ChallengeImage, ChallengeIn, GG, GeneralCustomer, Sample, StaffProfile, TopManagement


class ChallengeImageInline(TabularInline):
    model = ChallengeImage
    extra = 1
    fields = ['image']


@admin.register(Sample)
class SampleAdmin(ModelAdmin):
    compressed_fields = True
    list_display    = ['style_number', 'buyer', 'sample_type', 'status', 'submission_date']
    list_filter     = ['status', 'buyer', 'brand', 'category']
    search_fields   = ['style_number', 'color', 'sample_type']
    list_filter_submit = True
    readonly_fields = ['style_number']
    inlines         = [ChallengeImageInline]
    fieldsets = (
        ('Basic Info', {
            'fields': ('style_number', 'sample_type', 'color', 'season', 'status', 'submission_date'),
        }),
        ('Relations', {
            'fields': ('buyer', 'maker', 'brand', 'category'),
        }),
        ('Technical Specs', {
            'fields': ('gg', 'weight', 'yarn_composition', 'yarn_consumption', 'moisture_level', 'description', 'challenge_in'),
        }),
        ('Images & Files', {
            'fields': ('front_part_image', 'back_part_image', 'tech_pack', 'documents'),
        }),
    )


@admin.register(Buyer)
class BuyerAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['buyer_name', 'user']
    search_fields = ['buyer_name', 'user__username']


@admin.register(StaffProfile)
class StaffProfileAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['user', 'emp_id', 'role', 'designation', 'phone_number']
    search_fields = ['user__username', 'emp_id', 'role', 'designation']
    list_filter   = ['role']


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['name', 'origin']
    search_fields = ['name', 'origin']
    list_filter   = ['origin']


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['name']
    search_fields = ['name']


@admin.register(GG)
class GGAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['title']
    search_fields = ['title']


@admin.register(ChallengeIn)
class ChallengeInAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['title']
    search_fields = ['title']


@admin.register(ChallengeImage)
class ChallengeImageAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['sample', 'image']
    search_fields = ['sample__style_number']


@admin.register(TopManagement)
class TopManagementAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['full_name', 'user', 'department', 'designation']
    search_fields = ['full_name', 'user__username', 'department', 'designation']


@admin.register(GeneralCustomer)
class GeneralCustomerAdmin(ModelAdmin):
    compressed_fields = True
    list_display  = ['user']
    search_fields = ['user__username']
