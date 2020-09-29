from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("jet/", include("jet.urls", "jet")),
    path("api/", include("auction_api.urls")),
] + static(settings.MEDIA_URL_PATH, document_root=settings.MEDIA_ROOT)
