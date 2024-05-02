from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,post
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
import os
from django.utils.html import format_html, mark_safe
from content_editor.contents import contents_for_item
from .forms import quillpost


#Web Personal
def personal(require):
    return render(require, 'personal.html' )
#Web Personal
def post_view(request):
    # Obtener todos los objetos 'post'
    posts = post.objects.all()
        # Pasar los campos a la plantilla 'blog_index.html'
    return render(request, 'blog_index.html', {
        'post': posts
    })


def crear_post(request): 
    if request.method == 'POST':
        form = quillpost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')  # Redirige a la página deseada después de guardar el formulario
    else:
        form = quillpost()
    
    return render(request, 'form_view.html', {'form': form})

def blogs(request,id):
    usuario=post.objects.get(id=id).usuario
    fecha=post.objects.get(id=id).fecha
    titulo=post.objects.get(id=id).titulo
    contenido=post.objects.get(id=id).contenido
    bibliografia=post.objects.get(id=id).bibliografia

    return render(request, 'blogs.html', {'usuario':usuario,'fecha':fecha,'titulo':titulo,'contenido':contenido,'bibliografia':bibliografia,} )
