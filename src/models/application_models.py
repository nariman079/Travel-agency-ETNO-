from django.db import models

from src.services.application_services import SendMessageAboutApplication


class ApplicationTour(models.Model):
    """
    Модель заявок
    """
    class Meta:
        db_table = 'application_tour'
        verbose_name = "Заявка на тур"
        verbose_name_plural = "Заявки на туры"

    full_name = models.CharField(max_length=60, verbose_name="Полное имя")
    phone_number = models.CharField(max_length=60, verbose_name="Номер телефона")
    tour = models.ForeignKey('src.Tour', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.pk:
            body = dict(
                full_name=self.full_name,
                phone_number=self.phone_number,
                tour_title=self.tour.title
            )
            SendMessageAboutApplication(body).execute()
        return super().save(*args, **kwargs)
