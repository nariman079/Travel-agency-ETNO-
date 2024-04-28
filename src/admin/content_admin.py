from django.contrib import admin


class ContentManagementArea(admin.AdminSite):
    site_header = "Управление контентом"


content_management_admin = ContentManagementArea(name="Content management")

