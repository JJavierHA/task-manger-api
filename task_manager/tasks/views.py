# from django.shortcuts import render
from rest_framework import viewsets
from .models import Task # importamos los modelos
from .serializers import TaskSerializer # importamos el serializador creado

# establecemos las vistas de la API
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() # Establecemos los elementos del modelo seleccionado
    serializer_class = TaskSerializer # establecemos la clase serilizadora que tomara como base

#! Nota: (viewsets.ModelViewSet) implementa las operaciones crud sin tener que realizarlas manualmente