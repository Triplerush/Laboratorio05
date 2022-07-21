from logging import PlaceHolder
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
  nombres = forms.CharField(
    widget = forms.Textarea(
      attrs = {
        'placeholder' : 'Sólo tu nombre, por favor',
        'id': 'nombreID',
        'class' : 'special',
        'cols' : '10',
      }
    )
  )

  apellidos = forms.CharField()
  edad = forms.IntegerField(initial=25)
  donador = forms.BooleanField()