from django.db import models
from django.db.models.signals import pre_save 
from django.dispatch import receiver 
from django.utils import timezone

class Drivers(models.Model):
    driverName = models.CharField(max_length=30, verbose_name='Имя водителя')
    driverSurname = models.CharField(max_length=30, verbose_name='Фамилия водителя')
    class Meta:
        verbose_name=verbose_name_plural='Водители карет'

class Cars(models.Model):
    car_driver = models.ForeignKey(Drivers, on_delete=models.PROTECT)
    carNumber = models.CharField(max_length=6, verbose_name='Гос. номер авто')

    class Meta:
        verbose_name=verbose_name_plural='Зарегистрированные кареты'

class Medics(models.Model):
    car_id = models.ForeignKey(Cars, on_delete=models.PROTECT, default=None)
    medicName = models.CharField(max_length=30, verbose_name='Имя врача')
    medicSurname = models.CharField(max_length=30, verbose_name='Фамилия врача')
    medic_position = models.CharField(max_length=15, verbose_name='Должность врача')
    is_working = models.BooleanField(default=False, verbose_name='На смене')
    class Meta:
        verbose_name=verbose_name_plural= 'Мед.работники'

class Clients(models.Model):
    SEX_CHOICES=[
        ("M", "Male"),
        ("F", "Female")
    ]

    clientName = models.CharField(max_length=30, verbose_name='Имя клиента')
    clientSurname = models.CharField(max_length=30, verbose_name='Фамилия клиента')
    phoneNumber = models.CharField(max_length=11, unique=True, verbose_name='Номер телефона')
    age = models.IntegerField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)

    password = models.CharField(max_length=255, verbose_name='Пароль пользователя', default='0')
    class Meta:
        verbose_name=verbose_name_plural='Клиенты'

class Calls(models.Model):
    car_id = models.ForeignKey(Cars, on_delete=models.PROTECT, verbose_name='id кареты', blank=True)
    client_id = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='id клиента')
    address = models.CharField(max_length=40, verbose_name='Адрес вызова')
    client_phone = models.ForeignKey(Clients, to_field='phoneNumber', related_name='client_phones', on_delete=models.PROTECT)

    diagnose = models.CharField(max_length=40, verbose_name='Предварительный диагноз при вызове')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время поступления вызова')
    time_accepted = models.DateTimeField(auto_now=True, verbose_name='Время принятия вызова')
    time_arrived = models.DateTimeField(auto_now=True, verbose_name='Время прибытия на вызов')
    category = models.IntegerField(default=3)
    is_accepted = models.BooleanField(default=False)
    is_arrived = models.BooleanField(default=False)

    class Meta:
        verbose_name= verbose_name_plural = 'Таблица вызовов'
