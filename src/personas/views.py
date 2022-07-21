from django.shortcuts import render,get_object_or_404,redirect
from .models import Persona
from django.views.generic.list import ListView
from .forms import PersonaForm, RawPersonForm
#Create your views here.
class PersonaListView(ListView):
  model = Persona

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

def personasShowObject(request, myId):
  obj = get_object_or_404(Persona,id=myId)
  context = {
    'objeto': obj
  }
  return render(request,'personas/descripcion.html',context)

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
  
def personasDeleteView(request, myId):
  obj = get_object_or_404(Persona, id = myId)
  if request.method == "POST":
    print("Lo borro")
    obj.delete ()
    return redirect('/')
  context = {
    'objeto': obj
  }
  return render(request, 'personas/personasBorrar.html', context)

def personasListView(request):
  queryset = Persona.objects.all()
  context = {
    'list': queryset,
  }
  return render(request,'personas/personasLista.html',context)

def searchForHelp(request):
  return render(request,'personas/search.html',{})