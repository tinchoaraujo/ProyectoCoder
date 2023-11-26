from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField(unique=True)

    def __str__(self):
        return f'Equipo: {self.nombre}, Codigo: {self.codigo}'


class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Simpatizantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()