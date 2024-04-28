from django.contrib import admin
from src.models import application_models


class ApplicationCollectArea(admin.AdminSite):
    site_header = "Заявки"


application_collection_admin = ApplicationCollectArea(name="Application admin")


class ApplicationAdminPanel(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')


application_collection_admin.register(application_models.ApplicationTour, ApplicationAdminPanel)
