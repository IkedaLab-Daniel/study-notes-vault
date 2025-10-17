from django.contrib import admin
from .models import Drinks, DrinkCategory, Booking

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinkCategory)
admin.site.register(Booking)