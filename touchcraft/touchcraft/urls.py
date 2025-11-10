from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.http import FileResponse
import os

# Путь к файлу app-ads.txt
APP_ADS_PATH = "app-ads.txt"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # jet urls
    # URL для смены языка
    path('i18n/', include('django.conf.urls.i18n')),

    # Отдаём app-ads.txt напрямую
    path("app-ads.txt", lambda request: FileResponse(open(APP_ADS_PATH, "rb"), content_type="text/plain")),
]

urlpatterns += i18n_patterns(

    path('', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
