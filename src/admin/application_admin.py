from django.contrib import admin


class ApplicationCollectArea(admin.AdminSite):
    site_header = "Заявки"


application_collection_admin = ApplicationCollectArea(name="Application admin")

