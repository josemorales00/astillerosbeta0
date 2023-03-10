from django.db import models

# Create your models here.
class Datos(models.Model):
    id = models.BigAutoField(primary_key=True)
    deveui = models.CharField(db_column='DevEUI', max_length=20)  # Field name made lowercase.
    devaddr = models.CharField(db_column='devAddr', max_length=15)  # Field name made lowercase.
    datos = models.CharField(db_column='Datos', max_length=100)  # Field name made lowercase.
    consumo = models.DecimalField(db_column='Consumo', max_digits=10, decimal_places=4)  # Field name made lowercase.
    fechamed = models.DateTimeField(db_column='FechaMed', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datos'