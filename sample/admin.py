from django.contrib import admin
from .models import Buyer, Sample, StaffProfile


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'buyer', 'maker', 'submission_date']
    list_filter = ['buyer', 'maker']
    search_fields = ['product_name']


admin.site.register(Buyer)
admin.site.register(StaffProfile)
