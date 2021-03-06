from django.db import models
from django.contrib.auth.models import User
from django.db.models import F


class Offer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор обьявления', null=True, blank=True)
    price = models.IntegerField('Цена', null=True, blank=True)
    price_percent = models.IntegerField(null=True, blank=True)
    address = models.CharField('Адрес', max_length=15, null=True, blank=True)
    floor = models.IntegerField('Этаж', null=True, blank=True)
    rooms = models.IntegerField('Количество комнат', null=True, blank=True)
    area = models.IntegerField('Площадь')
    floor_count = models.IntegerField('Количество этажей', null=True, blank=True)
    property_type = models.CharField('Тип собственности', max_length=15, null=True, blank=True)

    class Meta:
        verbose_name='предложение'
        verbose_name_plural='Предложения'

class Req(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор обьявления', null=True, blank=True)
    min_price = models.IntegerField('Цена от', blank=True, null=True)
    max_price = models.IntegerField('До', blank=True, null=True)
    min_area = models.IntegerField('Минимальная площадь (кв. метров)', blank=True, null=True)
    max_area = models.IntegerField('Максимальная площадь (кв. метров)', blank=True, null=True)
    min_room_count = models.IntegerField('Минимальное количество комнат', blank=True, null=True)
    max_room_count = models.IntegerField('Максимальное количество комнат', blank=True, null=True)
    min_floor = models.IntegerField('Этаж от', blank=True, null=True)
    max_floor = models.IntegerField('До', blank=True, null=True)
    min_floor_count = models.IntegerField('Количество этажей от', blank=True, null=True)
    max_floor_count = models.IntegerField('До', blank=True, null=True)
    property_type = models.CharField('Тип имущества', max_length=15, blank=True, null=True)


    class Meta:
        verbose_name='запрос'
        verbose_name_plural='запросы'

class Client(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', null=True, blank=True)
    first_name = models.CharField('Имя', max_length=15, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=15, null=True, blank=True)
    middle_name = models.CharField('Отчество', max_length=15, null=True, blank=True)
    phone = models.IntegerField('Телефон', blank=True, null=True)
    email = models.CharField('Email', max_length=15, null=True, blank=True)

class Realtor(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто добавил', null=True, blank=True)
    first_name = models.CharField('Имя', max_length=15, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=15, null=True, blank=True)
    middle_name = models.CharField('Отчество', max_length=15, null=True, blank=True)
    commission = models.IntegerField('Комиссия', blank=True, null=True)

class Deal(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    req = models.ForeignKey(Req, on_delete=models.CASCADE, null=True, blank=True)