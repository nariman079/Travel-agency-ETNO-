from django.contrib import admin
from src.models import ApplicationTour, Report
from src.services.tour_services import create_report

class ApplicationCollectArea(admin.AdminSite):
    site_header = "Заявки"


application_collection_admin = ApplicationCollectArea(name="Application admin")


class ApplicationAdminPanel(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number')

class ReportAdminPanel(admin.ModelAdmin):
    list_display = ('uid', 'report_type', 'url')

    def save_model(self, obj: Report, *args, **kwargs):
        create_report(obj)
        super().save_model(obj, *args, **kwargs)

application_collection_admin.register(ApplicationTour, ApplicationAdminPanel)
application_collection_admin.register(Report, ReportAdminPanel)