from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    slot = models.CharField(default='morning',max_length=100)
    cardio = models.BooleanField(default=False)
    weight = models.FloatField()
    image = models.ImageField(upload_to="images/")
