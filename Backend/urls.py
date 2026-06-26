from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("", include("Base.urls")),
    path("", include("auths.urls")),
    # path("", include("main.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
