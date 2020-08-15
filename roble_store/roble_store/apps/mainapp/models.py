# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#objects = models.Manager()


   
class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(db_column='nombreCategoria', max_length=100)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    objects = models.Manager()



class Productos(models.Model):
    objects = models.Manager()
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length=200)  # Field name made lowercase.
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idProveedor', blank=True, null=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='idCategoria', blank=True, null=True)  # Field name made lowercase.
    presentacion = models.CharField(max_length=50, blank=True, null=True)
    preciounidad = models.DecimalField(db_column='precioUnidad', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unidadesenexistencia = models.SmallIntegerField(db_column='unidadesEnExistencia', blank=True, null=True)  # Field name made lowercase.
    unidadesenpedido = models.SmallIntegerField(db_column='unidadesEnPedido', blank=True, null=True)  # Field name made lowercase.
    fechacompra = models.DateField(db_column='fechaCompra', blank=True, null=True)  # Field name made lowercase.
    fechaexpiracion = models.DateField(db_column='fechaExpiracion', blank=True, null=True)  # Field name made lowercase.
    costoestimado = models.DecimalField(db_column='costoEstimado', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    srcimagen = models.CharField(db_column='srcImagen', max_length=100, blank=True, null=True)  # Field name made lowercase.
    suspendido = models.SmallIntegerField(blank=True, null=True)

class Proveedores(models.Model):
    idproveedor = models.AutoField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=60)  # Field name made lowercase.
    rucempresa = models.CharField(db_column='rucEmpresa', max_length=15, blank=True, null=True)  # Field name made lowercase.
    direccionempresa = models.CharField(db_column='direccionEmpresa', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sucursalempresa = models.CharField(db_column='sucursalEmpresa', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonoempresa = models.CharField(db_column='telefonoEmpresa', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emailempresa = models.CharField(db_column='emailEmpresa', max_length=35, blank=True, null=True)  # Field name made lowercase.
    nombrecontacto = models.CharField(db_column='nombreContacto', max_length=35, blank=True, null=True)  # Field name made lowercase.
    telefonocontactouno = models.CharField(db_column='telefonoContactoUno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonocontactodos = models.CharField(db_column='telefonoContactoDos', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emailcontacto = models.CharField(db_column='emailContacto', max_length=35, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)