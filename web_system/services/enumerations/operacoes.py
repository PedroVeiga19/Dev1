from django.db import models


class Operacoes(models.TextChoices):
    ADDITION = "+", "Adição"
    SUBTRACION= "-", "Subtração"
    MULTIPLICATION = "*", "Multiplicação"
    DIVISION = "/", "Divisão"