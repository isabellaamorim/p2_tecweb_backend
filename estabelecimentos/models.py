from django.db import models


class Estabelecimento(models.Model):
    name = models.CharField(max_length=200)
    adress = models.TextField()