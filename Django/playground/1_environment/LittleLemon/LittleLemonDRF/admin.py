from atexit import register

from django.contrib import admin
from .models import MenuItem
# Register your models here.

admin.site,register(MenuItem)