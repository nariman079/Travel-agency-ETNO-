from rest_framework.routers import SimpleRouter
from src.views.application_views import ApplicationTourViewSet

application_router = SimpleRouter()
application_router.register(r'', ApplicationTourViewSet.as_view())