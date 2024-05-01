from django import forms
from .models import post
from django_quill.fields import QuillField

class quillpost(forms.ModelForm):
    contenido = QuillField()

    class Meta:
        model = post
        fields = ['usuario','titulo','reseña','contenido', 'bibliografia','fecha']
