from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from Etno import settings
from Etno.services import convert_images, test_get_attr
from ture.models import Image
urlpatterns = [
    path('', main_page , name="main-page"),
    path('tour/<int:id>/',tour , name="tour" ),
    path('gallery/', gallery, name="gallery"),
    path('about/', about, name="about")
] 


