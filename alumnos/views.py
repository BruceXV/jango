from django.shortcuts import render

from .models import Genero,Alumno
# Create your views here.

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def alumnos_edit(request):
    context={}
    return render(request,"alumnos/alumnos_edit.html",context)

def alumnos_add(request):
    context={}
    return render(request,"alumnos/alumnos_add.html",context)

def alumnos_list(request):
    context={}
    return render(request,"alumnos/alumnos_list.html",context)