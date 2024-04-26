from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class blog(models.Model):
    descripcion = models.TextField()
    titulo = models.CharField(max_length=150)
        

class noticias(models.Model):
    encabezado = models.TextField()
    titulo = models.CharField(max_length=150)
    parrafo = models.CharField(max_length=300)

class tareas(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
     
    