from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria') 
    nombreCategoria=models.CharField(max_length=30, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria


class Gato(models.Model):
    chip=models.CharField(max_length=6, primary_key=True, verbose_name='Chip')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    raza=models.CharField(max_length=20, verbose_name='Raza')
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.chip

class Cliente(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    numero=models.CharField(max_length=20, verbose_name='Numero')

    def __str__(self):
        return self.rut