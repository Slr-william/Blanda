from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import FloatField

class objeto(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class caracteristica(models.Model):
    feature = models.CharField(max_length = 50)

    def __str__(self):
        return self.feature

class objetoCaracteristica(models.Model):
    obj = models.ForeignKey(objeto, on_delete=models.CASCADE)
    fea = models.ForeignKey(caracteristica, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.obj.name, self.fea.feature)
