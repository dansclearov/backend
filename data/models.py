from django.db import models


class Bin(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    percentage = models.IntegerField()
