from django.contrib import admin
from .models import Brand, Buyer, Category, ChallengeIn, GG, Sample, StaffProfile


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'buyer', 'maker', 'submission_date']
    list_filter = ['buyer', 'maker']
    search_fields = ['product_name']


admin.site.register(Buyer)
admin.site.register(StaffProfile)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(GG)
admin.site.register(ChallengeIn)
