from django.db import models
class Games (models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=200, default="")


# Create your models here.
