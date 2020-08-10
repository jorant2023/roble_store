# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#objects = models.Manager()

class Banco(models.Model):
    idbanco = models.AutoField(db_column='idBanco', primary_key=True)  # Field name made lowercase.
    nombrebanco = models.CharField(db_column='nombreBanco', max_length=35)  # Field name made lowercase.
    telefonobanco = models.CharField(db_column='telefonoBanco', max_length=15, blank=True, null=True)  # Field name made lowercase.

class Cabecerapedidos(models.Model):
    idcabecerapedido = models.AutoField(db_column='idCabeceraPedido', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.
    idempleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='idEmpleado', blank=True, null=True)  # Field name made lowercase.
    fechapedido = models.DateTimeField(db_column='fechaPedido', blank=True, null=True)  # Field name made lowercase.
    fechaconfirmacion = models.DateTimeField(db_column='fechaConfirmacion', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='fechaEntrega', blank=True, null=True)  # Field name made lowercase.
    iddelivery = models.ForeignKey('Delivery', models.DO_NOTHING, db_column='idDelivery', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    direcciondestinatario = models.CharField(db_column='DireccionDestinatario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ciudaddestinatario = models.CharField(db_column='CiudadDestinatario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    regiondestinatario = models.CharField(db_column='RegionDestinatario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    codpostaldestinatario = models.CharField(db_column='CodPostalDestinatario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    paisdestinatario = models.CharField(db_column='PaisDestinatario', max_length=60, blank=True, null=True)  # Field name made lowercase.

   
class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(db_column='nombreCategoria', max_length=100)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    objects = models.Manager()
class Clientes(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=20)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=35, blank=True, null=True)
    telefonouno = models.CharField(db_column='telefonoUno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonodos = models.CharField(db_column='telefonoDos', max_length=15, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=60, blank=True, null=True)
    ciudad = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    codigopostal = models.CharField(db_column='codigoPostal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)

class Delivery(models.Model):
    iddelivery = models.AutoField(db_column='idDelivery', primary_key=True)  # Field name made lowercase.
    nombredelivery = models.CharField(db_column='nombreDelivery', max_length=100)  # Field name made lowercase.
    telefono = models.CharField(max_length=15, blank=True, null=True)
    dnidelivery = models.CharField(db_column='dniDelivery', max_length=15, blank=True, null=True)  # Field name made lowercase.

class Detallepedidos(models.Model):
    iddetallepedidos = models.AutoField(db_column='idDetallePedidos', primary_key=True)  # Field name made lowercase.
    idcabecerapedido = models.ForeignKey(Cabecerapedidos, models.DO_NOTHING, db_column='idCabeceraPedido', blank=True, null=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idProducto', blank=True, null=True)  # Field name made lowercase.
    preciounidad = models.DecimalField(db_column='precioUnidad', max_digits=10, decimal_places=2)  # Field name made lowercase.
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Empleados(models.Model):
    idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=35, blank=True, null=True)
    dni = models.CharField(max_length=15)
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechacontratacion = models.DateField(db_column='FechaContratacion', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=60, blank=True, null=True)
    ciudad = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    telefonofijo = models.CharField(db_column='telefonoFijo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonomovil = models.CharField(db_column='telefonoMovil', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idbanco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='idBanco', blank=True, null=True)  # Field name made lowercase.
    numerocuentabancaria = models.CharField(db_column='numeroCuentaBancaria', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sueldobasico = models.DecimalField(db_column='sueldoBasico', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descuentos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

class Productos(models.Model):
    objects = models.Manager()
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='nombreProducto', max_length=40)  # Field name made lowercase.
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
    idproveedor = models.IntegerField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
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