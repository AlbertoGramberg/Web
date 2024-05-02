from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django_quill.fields import QuillField



class blog(models.Model):
    descripcion = models.TextField()
    titulo = models.CharField(max_length=150)
        

class post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Asigna un usuario 
    titulo = models.CharField(max_length=200)
    reseña=models.TextField(max_length=400)
    contenido = QuillField()
    bibliografia = QuillField()
    fecha = models.DateTimeField(default=timezone.now)
    
   

    def __str__(self):
        return self.titulo
    

     
