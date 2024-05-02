from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.personal),
    path('web/', views.personal, name='personal'),
    path('blog/', views.post_view, name=''),
    path('blog/<int:id>', views.blogs, name=''),
    path('formulario/', views.crear_post, name='crear_post'),



    
] 
    
