from django.db import models


class Client(models.Model):
    client_id = models.IntegerField('ID клиента')
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30)
    phone_number = models.CharField('Телефонный номер', max_length=30)
    email = models.CharField('Почта', max_length=30)
    password = models.CharField('Пароль', max_length=15)


class Realtor(models.Model):
    realtor_id = models.IntegerField('ID риелтора')
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    middle_name = models.CharField('Отчество', max_length=30)
    email = models.CharField('Почта', max_length=30)
    password = models.CharField('Пароль', max_length=15)
    comission = models.IntegerField('Комиссия')


class Offer(models.Model):
    offer_id = models.IntegerField('ID')
    client_id = models.IntegerField('ID клиента')
    realtor_id = models.IntegerField('ID риелтора')
    price = models.IntegerField('Цена')
    address = models.CharField('Имя', max_length=25)
    floor = models.IntegerField('Номер этажа')
    rooms = models.IntegerField('Количество комнат')
    area = models.IntegerField('Площадь (кв. метров)')
    floor_count = models.IntegerField('Количество этажей')
    type_of_property = models.CharField('Тип имущества', max_length=15)
    coordinates = models.CharField('Координаты', max_length=100)


class Requirement(models.Model):
    requirement_id = models.IntegerField('ID')
    client_id = models.IntegerField('ID клиента')
    realtor_id = models.IntegerField('ID риелтора')
    min_price = models.IntegerField('Цена от')
    max_price = models.IntegerField('До')
    min_area = models.IntegerField('Минимальная площадь (кв. метров)')
    max_area = models.IntegerField('Максимальная площадь (кв. метров)')
    min_room_count = models.IntegerField('Минимальное количество комнат')
    max_room_count = models.IntegerField('Максимальное количество комнат')
    min_floor = models.IntegerField('Этаж от')
    max_floor = models.IntegerField('До')
    min_floor_count = models.IntegerField('Количество этажей от')
    max_floor_count = models.IntegerField('До')
    type_of_property = models.CharField('Тип имущества', max_length=15)


class Deal(models.Model):
    offer_id = models.IntegerField('ID предложения')
    requirement_id = models.IntegerField('ID запроса')