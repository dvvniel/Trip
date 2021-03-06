from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

class Rol(models.Model):
    id_rol_usuario = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=14)

class Usuario(models.Model):
    usuario = models.CharField(primary_key=True,max_length=20,null=False,blank=False)
    nombre = models.CharField(max_length=20,null=False,blank=False)
    apellido = models.CharField(max_length=20,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    contrasena = models.CharField(max_length=30,null=False,blank=False)
    foto_perfil = models.ImageField(null=True,blank=True,upload_to = 'uploads')
    desc_perfil = models.CharField(max_length=50,null=True,blank=True)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50,null=False,blank=False) 
    desc_post = models.CharField(max_length=150,null=False,blank=False)
    foto_post = models.ImageField(null=False,blank=False,upload_to='uploads')
    fecha_publicacion = models.DateTimeField()
    visitas = models.IntegerField()
    usuario2 = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta:
        # sort by "fecha" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-fecha_publicacion']


class Comentarios(models.Model):
    id_comentarios = models.AutoField(primary_key=True)
    desc_comentarios = models.CharField(max_length=100,null=True,blank=False)
    fecha_comentario = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        # sort by "fecha" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-fecha_comentario']

class Respuesta_Comentarios(models.Model):
    id_respuesta_c = models.AutoField(primary_key=True)
    r_comentario = models.CharField(max_length=100,null=True,blank=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    comentarios = models.ForeignKey(Comentarios,on_delete=models.CASCADE)

class Lugares(models.Model):
    id_lugares = models.AutoField(primary_key=True)
    nombre_lugar = models.CharField(max_length=40,null=False,blank=False)
    foto_lugares = models.ImageField(upload_to='uploads')
    desc_lugares = models.CharField(max_length=200,null=False,blank=False)
    status = models.IntegerField()



