from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sample.views import custom_404

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sample.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
