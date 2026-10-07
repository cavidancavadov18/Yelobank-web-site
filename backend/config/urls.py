from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

def health(_request):
    return JsonResponse({"ok": True})


urlpatterns = [
    path("health/", health),
    path("admin/", admin.site.urls),
    path("api/", include("content.urls")),
    path("api/", include("applications.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
