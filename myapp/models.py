from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from content_editor.models import Region, create_plugin_base
from django_quill.fields import QuillField


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

class post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Asigna un usuario 
    titulo = models.CharField(max_length=200)
    reseña=models.TextField(max_length=400)
    contenido = QuillField()
    bibliografia = QuillField()
    fecha = models.DateTimeField(default=timezone.now)
    
   

    
class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(blank=True, null=True)

    # The ContentEditor requires a "regions" attribute or property
    # on the model. Our example hardcodes regions; if you need
    # different regions depending on other factors have a look at
    # feincms3's TemplateMixin.
    regions = [
        Region(key="main", title="main region"),
        Region(key="sidebar", title="sidebar region"),
    ]
class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comentarios')

ArticlePlugin = create_plugin_base(Article)


class RichText(ArticlePlugin):
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = "rich text"
        verbose_name_plural = "rich texts"


class Download(ArticlePlugin):
    file = models.FileField(upload_to="downloads/%Y/%m/")

    class Meta:
        verbose_name = "download"
        verbose_name_plural = "downloads"



    def __str__(self):
        return self.titulo
    

     
