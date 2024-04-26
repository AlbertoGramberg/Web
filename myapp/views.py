from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, noticias     
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.shortcuts import redirect
from googleapiclient.discovery import build
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from django.conf import settings
import os
from .palabras import lista_palabras
from .forms import PalabraForm
from .guardarpalabras import GuardarPalabras
from palabra import palabralista
# Create your views here.
API_KEY = "AIzaSyBg4WEYkkCog85Q8ES0x2AWojKNcEfe5s0"
def inicio(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Esto Es un texto de Prueba, en esta seccion encontrara Informacion acerca de Nosotros")

def project(request, id):
    #project = list(Project.objects.values())
    project = Project.objects.get(id=id)
    return HttpResponse('Project: %s' % project.name )


#def Noticias(request, id):
    #Noticias = noticias.objects.get(id=id)
    #return HttpResponse('Titulo: %s </br> Encabezado: %s </br> Parrafo: %s' % (Noticias.#titulo, Noticias.encabezado, Noticias.parrafo))
#def Noticias(request, id):
     #titulo = noticias.objects.get(id=id)
     #encabezado = noticias.objects.get(id=id)
     #parrafo = noticias.objects.get(id=id)
     #return render(request, 'noticias.html',{'titulo':titulo},{'encabezado':encabezado},{'parrafo':parrafo})
def Noticias(request, id):
    titulo = noticias.objects.get(id=id).titulo
    encabezado = noticias.objects.get(id=id).encabezado
    parrafo = noticias.objects.get(id=id).parrafo
    return render(request, 'noticias.html', {'titulo': titulo, 'encabezado': encabezado, 'parrafo': parrafo})



def Novedades(request):
    return HttpResponse("Esto Es un texto de Prueba, en esta seccion Novedades")

def buscar_videos(query, max_results=10):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    video_ids = []
    for item in response['items']:
        video_ids.append(item['id']['videoId'])
    video_details = youtube.videos().list(
        part="snippet",
        id=",".join(video_ids)
    ).execute()
    videos = []
    for item in video_details['items']:
        video = {
            'titulo': item['snippet']['title'],
            'url': f"https://www.youtube.com/watch?v={item['id']}",
            'id': item['id'],  # Almacenar solo el ID del video
            'miniatura': item['snippet']['thumbnails']['medium']['url']
        }
        videos.append(video)
    return videos
def lista_videos(request, palabra_busqueda):
    # Instancia de la clase GuardarPalabras()
    clase_palabras = GuardarPalabras()
    
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos recibidos
        form = PalabraForm(request.POST)
        # Verificar si el formulario es válido
        if form.is_valid():
            # Obtener la palabra ingresada por el usuario
            palabra = form.cleaned_data['palabra']
            # Llamar a los métodos para guardar la palabra
            clase_palabras.guardar_palabra(request)
            clase_palabras.guardar_palabra_en_archivo(palabra)
            # Redirigir a la misma página para evitar reenvíos de formulario
            # Construir la URL de redirección dinámicamente
            
    else:
        # Si la solicitud no es un POST, crear un formulario vacío
        form = PalabraForm()

    # Obtener la lista de palabras
    list_palabras = palabralista
    
    # Obtener los videos de YouTube
    videos_biologia_celular = buscar_videos(palabra_busqueda)

    # Renderizar la plantilla con los datos necesarios
    return render(request, 'videos.html', {'videos': videos_biologia_celular, 'palabras': list_palabras, 'form': form})




def generate_wordcloud(request):
    # Ruta al archivo de texto con las palabras
    file_name = 'palabras.txt'
    file_path = os.path.join(settings.BASE_DIR, 'myapp', file_name)

    # Lee el archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    comment_words = content
    stopwords = set(STOPWORDS)
    
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)
    
    # Guarda la imagen de la nube de palabras
    wordcloud_filename = 'wordcloud.png'
    wordcloud_path = os.path.join(settings.MEDIA_ROOT, wordcloud_filename)
    wordcloud.to_file(wordcloud_path)

    # Pasa la ruta de la imagen a la plantilla para mostrarla
    context = {'wordcloud_path': wordcloud_path}
    return render(request, 'wordcloud.html', context)

#Web Personal
def personal(require):
    return render(require, 'personal.html' )

