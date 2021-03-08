from django.db import models

# Create your models here.


class product(models.Model):

    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    screen = models.CharField(max_length=100)
    chipset = models.CharField(max_length=200)
    camera = models.CharField(max_length=1000)
    gpu = models.CharField(max_length=300)
    special = models.CharField(max_length=200)
    price = models.IntegerField()
