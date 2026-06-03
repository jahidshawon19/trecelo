from django.contrib import admin
from .models import Brand, Buyer, Category, ChallengeImage, ChallengeIn, GG, Sample, StaffProfile


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['style_number', 'buyer', 'submission_date']
    list_filter = ['buyer']
    search_fields = ['style_number']


admin.site.register(Buyer)
admin.site.register(StaffProfile)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(GG)
admin.site.register(ChallengeIn)
admin.site.register(ChallengeImage)
