"""
core URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static

from src.core.urls.web import urlpatterns as web_urlpatterns
from src.core.urls.api import urlpatterns as api_urlpatterns

urlpatterns = [
    *web_urlpatterns,
    *api_urlpatterns,
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
