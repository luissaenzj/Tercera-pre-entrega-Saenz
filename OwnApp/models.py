from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    codigo = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} --- {self.codigo}'   

class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    edad= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} --- {self.apellido}'   

class Requerimiento (models.Model):
    req= models.CharField(max_length=50)
    fechaReq= models.DateField()
    UserPro = models.BooleanField()

    def __str__(self):
        return f'{self.req}'  