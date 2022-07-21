from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
  class Meta:
    model=Persona
    fields=[
        'nombres',
        'apellidos',
        'edad',
        'donador',
        ]

class RawPersonForm(forms.Form):
  nombres = forms.CharField()
  apellidos = forms.CharField()
  edad = forms.IntegerField()
  donador = forms.BooleanField()