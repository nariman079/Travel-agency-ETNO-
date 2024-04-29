from django.urls import path, include
from django.conf.urls.static import static

from config import settings
from src.admin import content_admin, application_admin

urlpatterns = [
    path(
        'content-management/',
        content_admin.content_management_admin.urls,
        name="content-management"
    ),
    path(
        'application-collect/',
        application_admin.application_collection_admin.urls,
        name="application-collect"
    ),
    path('', include('src.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
