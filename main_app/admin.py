from django.contrib import admin
from .models import Calls, Drivers, Cars

@admin.register(Calls)
class CallsAdmin(admin.ModelAdmin):
    pass


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    pass

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    pass


