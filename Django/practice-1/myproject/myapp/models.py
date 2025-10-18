from django.db import models

# Create your models here.
class DrinkCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField() 
    category_id = models.ForeignKey(DrinkCategory, on_delete=models.PROTECT, default=None)

# > Lab 7
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

# > Lab 8
class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name # > Employee first name will be display instead of "employee object"