from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return HttpResponse("Darjeeling Homestay Platform is running successfully!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homestays.urls")),
    path("", include("accounts.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
