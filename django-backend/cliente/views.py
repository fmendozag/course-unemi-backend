from django.shortcuts import render
from cliente.models import *
from django.http import HttpResponse

<<<<<<< HEAD
# Create your views here.
def create(request):
    grupo = ClienteGrupo(codigo= "000563",nombre="Empleados")
    grupo.save()
    return HttpResponse("Objeto creado correctamente")



=======
>>>>>>> 12ec5220c181461aaa421d68e84071bb625ed608
