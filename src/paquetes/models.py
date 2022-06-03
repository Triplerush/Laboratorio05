from django.db import models

# Create your models here.
class Paquete(models.Model):

    persona = models.EmailField(max_length = 254)
    fecha_inicio = models.DateField(auto_now_add = True) 
    identificador = models.CharField(max_length=10)
    entregado = models.BooleanField(
        default= False
    )
    peso = models.IntegerField()