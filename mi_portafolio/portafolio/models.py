from django.db import models

class Nav(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class SobreMi(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Hobbie(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Footer(models.Model):
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto
