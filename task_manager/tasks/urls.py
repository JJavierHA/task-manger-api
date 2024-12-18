from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet # importamos la vista -> (viewset)

router = DefaultRouter() # crea todas las rutas necesarias para la operacion crud
# establecera 'tasks' -> 'tasks/' como ruta para las operaciones crud
router.register(r'tasks', TaskViewSet) 

urlpatterns = [
    path("", include(router.urls)),
]