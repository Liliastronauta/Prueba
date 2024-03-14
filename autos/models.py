from django.db import models

# Create your models here.

class Auto(models.Model):
    modelo = models.CharField(max_length= 100, verbose_name="Modelo del automovil")
    marca = models.CharField(max_length=100, verbose_name= "Marca del automovil")
    color = models.CharField(max_length= 100, verbose_name= "Color del vehiculo")
    año = models.IntegerField(verbose_name="año del modelo")

    class Meta:
        db_table='Auto'



