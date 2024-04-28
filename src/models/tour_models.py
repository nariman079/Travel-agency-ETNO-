from django.db import models


class Tour(models.Model):
    img = models.ImageField(upload_to="img/")
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=60)
    img = models.ImageField(upload_to="img/")
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Attraction(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img_1 = models.ImageField(upload_to='img/')
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

