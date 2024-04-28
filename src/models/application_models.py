from django.db import models


class ApplicationTour(models.Model):
    class Meta:
        db_table = 'application_tour'
        verbose_name = "Заявки на тур"

    full_name = models.CharField(max_length=60, verbose_name="Полное имя")
    phone_number = models.CharField(max_length=60, verbose_name="Номер телефона")
    tour = models.ForeignKey('src.Tour', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.pk:
            # @todo добавить действие при создании заявки
            ...
        return super().save(*args, **kwargs)