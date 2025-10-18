from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
