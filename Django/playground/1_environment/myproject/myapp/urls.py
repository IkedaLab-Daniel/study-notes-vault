from django.urls import path
from myapp.views import Menu, About

urlpatterns = [
    path('about', view=About, name="about"),
    path('menu', view=Menu, name="Menu")
]