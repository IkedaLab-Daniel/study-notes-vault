from django.contrib import admin
from .models import MenuItem
from .models import Category

admin.site.register(MenuItem)
admin.site.register(Category)