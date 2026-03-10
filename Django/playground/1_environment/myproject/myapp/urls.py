from django.urls import path
from myapp.views import menu

urlpatterns = [
    path('menu', view=menu, name="menu"),
]