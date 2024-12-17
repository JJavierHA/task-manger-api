from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOISE = [
        ('PENDING', 'Pendiente'),
        ('IN_PROGRESS', 'En Proceso'),
        ('COMPLETED', 'Completada'),
    ]

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOISE, default='PENDING')
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # asignamos una tarea el id del usuario creador

    def __str__(self):
        return self.title
