from rest_framework import serializers # importamos el serializador de djangoRest
from .models import Task

# creamos la clase serializadora
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task # establecemos el modelo 
        fields = '__all__' # seleccionamos los campos a serializar