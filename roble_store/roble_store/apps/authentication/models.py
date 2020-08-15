from django.db import models

# Create your models here.

class Clientes(models.Model):
    #objects = models.Manager()
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=20)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=150, blank=True, null=True)
    telefonouno = models.CharField(db_column='telefonoUno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonodos = models.CharField(db_column='telefonoDos', max_length=15, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=60, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    codigopostal = models.CharField(db_column='codigoPostal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)
    email = models.CharField(db_column='email', max_length=150)
