from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
