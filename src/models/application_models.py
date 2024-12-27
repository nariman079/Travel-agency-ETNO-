from django.db import models


def max_value_validator(value: int):
    if value > 5:
        raise ValueError("Максимальное значение 5")
    return value

class ApplicationTour(models.Model):
    """
    Модель заявок
    """
    class Meta:
        db_table = 'application_tour'
        verbose_name = "Заявка на тур"
        verbose_name_plural = "Заявки на туры"

    class Status(models.TextChoices):
        new = 'new', "Новый"
        in_process = 'in-process', "В обработке"
        processed = 'processed', "Обработан"
        done = 'done', "Готово", 

    full_name = models.CharField(max_length=60, verbose_name="Полное имя")
    phone_number = models.CharField(max_length=60, verbose_name="Номер телефона")
    tour = models.ForeignKey('src.Tour', on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=Status.choices, default='new')
    date_created = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self) -> str: 
        return f"{self.full_name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            pass
        return super().save(*args, **kwargs)


class Review(models.Model):
    """Модель отзыва"""

    class Meta:
        db_table = 'review'
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    application_tour = models.OneToOneField(ApplicationTour, on_delete=models.PROTECT)
    mark = models.PositiveIntegerField(validators=[max_value_validator])
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.application_tour.full_name}, {self.mark}"