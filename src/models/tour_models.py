from django.db import models
from uuid import uuid4

class Tour(models.Model):
    img = models.ImageField(upload_to="img/")
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title # type: ignore


class Attraction(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img_1 = models.ImageField(upload_to='img/')
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title # type: ignore


class Image(models.Model):
    title = models.CharField(max_length=60)
    img = models.ImageField(upload_to="img/")
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title # type: ignore

class ProgramTrip(models.Model):
    ordering = models.IntegerField(default=10)
    title = models.CharField(max_length=60)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Report(models.Model):
    """Модель Отчетов"""

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    class ReportType(models.TextChoices):
        day = 'day', "За день"
        week = 'week', "За неделю"
        month = 'month', "За месяц"
    
    uid = models.CharField(max_length=90, default=uuid4, editable=False)
    report_type = models.CharField("Отчет за", max_length=40, choices=ReportType.choices)
    file = models.FileField("Файл",upload_to='reports/', editable=False, null=True)
    url = models.URLField(null=True)
