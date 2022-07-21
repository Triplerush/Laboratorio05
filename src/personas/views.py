from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonForm
#Create your views here.

def personaTestView(request):
  obj = Persona.objects.get(id=1)
  context={
      'nombre':obj.nombres,
      'edad':obj.edad,
      'objeto': obj,
      }
  return render(request,'personas/descripcion.html',context)

def personaCreateView(request):
  initialValues = {
    'nombres': 'Hola',
  }
  form = PersonaForm(request.POST or None, initial =initialValues)
  if form.is_valid():
    form.save()
    form = PersonaForm()

  context={
      'form':form,
  }
  return render(request,'personas/personasCreate.html',context)

def anotherPersonaCreateView(request):
  form = RawPersonForm()
  if request.method == "POST":
    form = RawPersonForm(request.POST)
    if form.is_valid ():
      print(form.cleaned_data)
      Persona.objects.create(**form.cleaned_data)
    else:
      print(form.errors)

  context={
    'form':form,
  }
  return render(request,'personas/personasCreate.html',context)


def searchForHelp(request):
  return render(request,'personas/search.html',{})