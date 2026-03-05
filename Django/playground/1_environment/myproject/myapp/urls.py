from django.urls import path
from .views import home

urlpatterns = [
    path('test', view=home, name="home")
]