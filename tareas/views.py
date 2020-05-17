from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    tareas = Tarea.objects.all()
    
    form = FormTarea()

    if request.method == 'POST':
        form = FormTarea(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tareas': tareas, 'form': form}
    return render(request, "tareas/inicio.html",context)


def editar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    
    form = FormTarea(instance=tarea)

    if request.method=='POST':
        form = FormTarea(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea.html', context)


def eliminar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)

    if request.method=='POST':
        tarea.delete()
        return redirect('/')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea.html', context)