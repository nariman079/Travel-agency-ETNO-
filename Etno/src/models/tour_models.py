from django.db.models import *


class Tour(Model):
    img = ImageField(upload_to="img/")
    title = CharField(max_length=60)
    description = TextField()
    price = IntegerField()

    def __str__(self) -> str:
        return self.title


class Image(Model):
    title = CharField(max_length=60)
    img = ImageField(upload_to="img/")
    tour_id = ForeignKey(Tour, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title


class Attraction(Model):
    title = CharField(max_length=30)
    description = TextField()
    img_1 = ImageField(upload_to='img/')
    img_2 = ImageField(upload_to='img/')
    tour_id = ForeignKey(Tour, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title

