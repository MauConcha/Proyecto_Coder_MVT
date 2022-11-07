from App1.models import Parientes
from django.shortcuts import render

# Create your views here.

def mostrar_familiares(request):

    a1 = Parientes(nombre='Pedro', apellido='Perez', edad=42, cumpleaños='1980-06-27', parentezco='Papá')

    a2 = Parientes(nombre='Carmen', apellido='Silva', edad=40, cumpleaños='1982-01-27', parentezco='Mamá')

    a3 = Parientes(nombre='Héctor', apellido='Perez', edad=12, cumpleaños='2010-01-27', parentezco='Hermano')

    return render(request, 'App1/familia.html', {'familiares':[a1, a2, a3]})