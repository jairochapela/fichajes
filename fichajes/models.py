from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fichaje(models.Model):
    entrada = models.fields.DateTimeField()
    salida = models.fields.DateTimeField(blank=True,null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} {self.entrada}"