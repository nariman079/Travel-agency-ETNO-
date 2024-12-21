from django.db import models


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