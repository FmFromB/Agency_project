from django.db import models

class Offer(models.Model):
    price = models.IntegerField('Цена', null=True, blank=True)
    address = models.CharField('Адрес', max_length=15, null=True, blank=True)
    floor = models.IntegerField('Этаж', null=True, blank=True)
    rooms = models.IntegerField('Количество комнат', null=True, blank=True)
    area = models.IntegerField('Площадь')
    floor_count = models.IntegerField('Количество этажей', null=True, blank=True)
    property_type = models.CharField('Тип собственности', max_length=15, null=True, blank=True)

    #def __str__(self):
       # return self.property_type, self.address, self.price

    class Meta:
        verbose_name='предложение'
        verbose_name_plural='Предложения'
