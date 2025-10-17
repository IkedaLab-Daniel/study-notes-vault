from django.contrib import admin
from .models import Drinks, DrinkCategory

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinkCategory)