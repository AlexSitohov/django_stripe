from django.db.models import *


class Item(Model):
    name = CharField('Наименование', max_length=100)
    description = CharField('Описание', max_length=255)
    price = IntegerField()

    image = ImageField('Картинка', null=True, blank=True)

    date_time_created = DateTimeField('Дата создания товара', auto_now_add=True)

    def __str__(self):
        return self.name
