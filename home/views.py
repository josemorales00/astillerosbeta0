from django.http import HttpResponse
from django.shortcuts import render
from .models import Datos
from subprocess import call


# Create your views here.
def homeView(request):
    return render(request,'home/tablacss.html')

def abrirAPI(request):
    call(['python', 'prueba.py'])
    return HttpResponse('CARPETA CREADA')

def tabla(request):
    datos = Datos.objects.all()
    return render(request, 'home/tablacss.html', {'datos': datos})