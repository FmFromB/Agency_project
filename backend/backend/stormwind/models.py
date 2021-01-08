from django.db import models

class Client(models.Model):
    first_name = models.CharField('Имя', max_length=30, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=300, blank=True, null=True)
    phone_number = models.CharField('Телефонный номер', max_length=300, blank=True, null=True)
    email = models.CharField('Почта', max_length=300, blank=True, null=True)
    password = models.CharField('Пароль', max_length=150, blank=True, null=True)

    def __str__(self):
        return "Client: {}, email: {}".format(self.first_name, self.email)


class Realtor(models.Model):
    first_name = models.CharField('Имя', max_length=30, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True, null=True)
    middle_name = models.CharField('Отчество', max_length=30, blank=True, null=True)
    email = models.CharField('Почта', max_length=30, blank=True, null=True)
    password = models.CharField('Пароль', max_length=15, blank=True, null=True)
    comission = models.IntegerField('Комиссия', blank=True, null=True)

    def __str__(self):
        return "Realtor: {}, email: {}".format(self.first_name, self.email)


class Offer(models.Model):
    client_id = models.IntegerField('ID клиента', blank=True, null=True)
    realtor_id = models.IntegerField('ID риелтора', blank=True, null=True)
    price = models.IntegerField('Цена', blank=True, null=True)
    address = models.CharField('Адрес', max_length=25, blank=True, null=True)
    floor = models.IntegerField('Номер этажа', blank=True, null=True)
    rooms = models.IntegerField('Количество комнат', blank=True, null=True)
    area = models.IntegerField('Площадь (кв. метров)', blank=True, null=True)
    floor_count = models.IntegerField('Количество этажей', blank=True, null=True)
    type_of_property = models.CharField('Тип имущества', max_length=15, blank=True, null=True)
    coordinates = models.CharField('Координаты', max_length=100, blank=True, null=True)

    def __str__(self):
        return "Adress: {}, price: {}, type: {}".format(self.address, self.price, self.type_of_property)


class Requirement(models.Model):
    client_id = models.IntegerField('ID клиента', blank=True, null=True)
    realtor_id = models.IntegerField('ID риелтора', blank=True, null=True)
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
    type_of_property = models.CharField('Тип имущества', max_length=15, blank=True, null=True)

    def __str__(self):
        return "Max price: {}, type: {}".format(self.max_price, self.type_of_property)


class Deal(models.Model):
    offer_id = models.IntegerField('ID предложения', blank=True, null=True)
    requirement_id = models.IntegerField('ID запроса', blank=True, null=True)