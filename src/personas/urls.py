from django.urls import path
from personas.views import (
    personaTestView,
    personaCreateView,
    searchForHelp,
    anotherPersonaCreateView,
    personasShowObject,
    personasListView,
    personasDeleteView
    )

app_name = 'personas'
urlpatterns = [
    path('persona/',personaTestView,name='Datos persona'),
    path('search/',searchForHelp,name='buscar'),
    path('agregar/',personaCreateView,name='formulario persona'),
    path('otroAgregar/',anotherPersonaCreateView,name='Otro formulario persona'),
    path('personas/<int:myId>/',personasShowObject,name='Datos persona'),
    path('personasList/',personasListView,name='Lista de personas'),
    path('borrar/<int:myId>/',personasDeleteView,name='Borrar persona'),
]