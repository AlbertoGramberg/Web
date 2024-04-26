from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from myapp.views import generate_wordcloud

urlpatterns = [
    path('', views.inicio),
    path('about/', views.about),
    path('novedades/', views.Novedades),
    path('projects/<int:id>', views.project),
    path('noticias/<int:id>', views.Noticias),
    path('video/', views.lista_videos),
    path('palabras/', views.generate_wordcloud, name='wordcloud'),
    path('videos/<str:palabra_busqueda>/', views.lista_videos, name='lista_videos'),
    path('web/', views.personal, name='personal')


    
] 
    
