from django.contrib import admin
from .models import Drinks, DrinkCategory, Booking, Employees

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinkCategory)
admin.site.register(Booking) # > Lab 7
admin.site.register(Employees) # > Lab 8