from django.db.models import *
from ture.models import Tour

class UserSendMessage(Model):
    fio = CharField(max_length=90)
    tel = CharField(max_length=20)
    tour = ForeignKey(Tour, on_delete=CASCADE)

    def __str__(self) -> str:
        return f"{self.tour} | ({self.tel}) | {self.fio} "