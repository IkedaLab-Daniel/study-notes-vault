from django.contrib import admin
from .models import Drinks, DrinkCategory, Booking, Employees, Menu

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinkCategory)
admin.site.register(Booking) # > Lab 7
admin.site.register(Employees) # > Lab 8
admin.site.register(Menu) # > Lab 11