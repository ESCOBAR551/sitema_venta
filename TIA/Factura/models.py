from django.db import models

class Cliente(models.Model):
    cedula_cliente = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.apellido
    

class Vendedor(models.Model): 
    cedula_vendedor = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True,max_length=5)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.id_categoria
    

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True,max_length=5)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True)
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.producto
    

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True,max_length=10)
    cedula_cliente= models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    cedula_vendedor= models.ForeignKey(Vendedor,on_delete=models.RESTRICT)
    id_producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)    
    catidade = models.DateField()
    iva = models.IntegerField()
    
    def __str__(self):
        return self.id_factura

