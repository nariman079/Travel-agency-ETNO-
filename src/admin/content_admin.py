from django.contrib import admin
from django.utils.html import format_html

from src.models import tour_models


class ContentManagementArea(admin.AdminSite):
    site_header = "Управление контентом"
    site_title = "Контент сайта"


content_management_admin = ContentManagementArea(name="Content management")


class TourAdminPanel(admin.ModelAdmin):
    list_display = ('image', 'title', 'price')

    def image(self, obj: tour_models.Tour) -> str:
        return format_html(
            f"""<img width="150" src="{obj.img.url}">"""
        ) or None


content_management_admin.register(tour_models.Tour, TourAdminPanel)


class AttractionAdminPanel(admin.ModelAdmin):
    list_display = ('image', 'title', 'tour_title')

    def tour_title(self, obj: tour_models.Attraction) -> str | None:
        return obj.tour_id.title or None

    def image(self, obj: tour_models.Attraction) -> str:
        return format_html(
            f"""<img width="150" src="{obj.img_1.url}">"""
        )


content_management_admin.register(tour_models.Attraction, AttractionAdminPanel)
content_management_admin.register(tour_models.Image)
