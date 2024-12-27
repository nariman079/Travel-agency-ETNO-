from django.urls import path, include

from src.views import tour_views
from src.routers import application_router

urlpatterns = [
    path('', tour_views.main_page , name="main-page"),
    path('tour/<int:id>/',tour_views.tour , name="tour" ),
    path('gallery/', tour_views.gallery, name="gallery"),
    path('about/', tour_views.about, name="about"),
    path('application-tour/', include(application_router.urls))
]


