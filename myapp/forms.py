# forms.py
from django import forms

class PalabraForm(forms.Form):
    palabra = forms.CharField(label='Palabra')