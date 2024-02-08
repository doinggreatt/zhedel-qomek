from django.db import models
from django.db.models.signals import pre_save 
from django.dispatch import receiver 
from django.utils import timezone
from django.db.models.signals import post_save
from django.db.models import Max

class Drivers(models.Model):
    driverName = models.CharField(max_length=30, verbose_name='Имя водителя')
    driverSurname = models.CharField(max_length=30, verbose_name='Фамилия водителя')
    class Meta:
        verbose_name=verbose_name_plural='Водители карет'

class Cars(models.Model):
    car_driver = models.ForeignKey(Drivers, on_delete=models.PROTECT)
    carNumber = models.CharField(max_length=6, verbose_name='Гос. номер авто')
    is_working = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.is_working:
            max_id_record = CarsPosition.objects.aggregate(max_id=Max('id'))
            max_id_value = max_id_record['max_id'] if max_id_record['max_id'] is not None else 0 
            CarsPosition.objects.create(id=max_id_value+1,car_id=self.id, lat=0, long=0)
        else:
            CarsPosition.objects.filter(car_id=self.id).delete()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        CarsPosition.objects.filter(car=self).delete()
        super().delete(*args, **kwargs)
    class Meta:
        verbose_name=verbose_name_plural='Зарегистрированные кареты'

class Calls(models.Model):
    id = models.IntegerField(primary_key = True)
    car_id = models.ForeignKey(Cars, on_delete=models.PROTECT, verbose_name='id кареты', null=True)
    client_name = models.CharField(max_length=30, default='0')
    address = models.CharField(max_length=100, verbose_name='Адрес вызова')
    
    client_phone = models.CharField(max_length=11)

    diagnose = models.CharField(max_length=40, verbose_name='Предварительный диагноз при вызове')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время поступления вызова')
    time_accepted = models.DateTimeField(verbose_name='Время принятия вызова', null=True)
    time_arrived = models.DateTimeField(verbose_name='Время прибытия на вызов', null=True)
    category = models.IntegerField(default=-1)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    is_accepted = models.BooleanField(default=False)
    is_arrived = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_accepted:
            self.time_accepted = timezone.now()

        if self.is_arrived:
            self.time_arrived = timezone.now()
        super().save(*args, **kwargs)
    class Meta:
        verbose_name= verbose_name_plural = 'Таблица вызовов'


class CarsPosition(models.Model):
    id = models.IntegerField(primary_key=True)
    car = models.ForeignKey(Cars, on_delete=models.PROTECT, verbose_name='id машины', unique=True)
    lat = models.FloatField()
    long = models.FloatField()
    is_free = models.BooleanField(default=True)
    call_address = models.CharField(default='None')

