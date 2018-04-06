from django.db import models


# Create your models here.
class Algo(models.Model):
    name = models.CharField(max_length=128)
    signal = models.CharField(max_length=256)
    trade = models.CharField(max_length=256)
    ticker = models.CharField(max_length=256)
