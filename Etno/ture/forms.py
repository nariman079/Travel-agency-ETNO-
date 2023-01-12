from django.forms import *


class GetEmailForm(Form):
    fio = CharField(max_length=90, widget=TextInput(attrs={'class':'fio', 'type':'text','placeholder':'ФИО', 'id':'fio'}))
    tel = CharField(max_length=20, widget=TextInput(attrs={'class':'phone', 'type':'tel','placeholder':'+7(920)-000-23-43', 'id':'tel'}))