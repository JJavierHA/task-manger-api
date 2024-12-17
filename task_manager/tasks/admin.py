from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]

admin.site.register(Task, TaskAdmin) # registramos la aplicaicon en el adminstrador de django