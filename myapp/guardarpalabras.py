from django.shortcuts import render
from .forms import PalabraForm
from django.shortcuts import redirect

class GuardarPalabras:
    @classmethod
    def guardar_palabra(cls, request):
        if request.method == 'POST':
            form = PalabraForm(request.POST)
            if form.is_valid():
                palabra = form.cleaned_data['palabra']
                cls.guardar_palabra_en_archivo(palabra)
                url_video = f'/videos/{palabra}'
                    # Redirigir a la URL construida
                    #return redirect(url_video)
                return redirect(url_video, url_video=url_video)
        else:
            form = PalabraForm()
        return render(request, 'formulario.html')

    @staticmethod
    def guardar_palabra_en_archivo(palabra):
        #se abre palabra.py
        with open('palabra.py', 'r') as archivo:
            #se se lee palabra como archivo y se le transfiera a una variable
            contenido = archivo.read()
        # se evalua si ya exite, si existe envia un mensaje de ya existe    
        if palabra in contenido:
            palabra_existe="La palabra ya existe, guardar otra"
            #return redirect('formulario.html', palabra_existe)
        #si no se agrega la palabra al archivo  palabras.py con la variable palabralista que contiene el array
        else:
            with open('palabra.py', 'a') as archivo:
                if contenido.strip() == "":
                    archivo.write(f"palabralista = ['{palabra}']")
                    
                else:
                    archivo.write(f", '{palabra}'")
                    
                    

    @staticmethod
    def palabra_existe(palabra):
        with open('palabra.py', 'r') as archivo:
            contenido = archivo.read()
            return palabra in contenido
