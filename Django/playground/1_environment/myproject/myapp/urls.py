from django.urls import path
from .views import home, about, menu, book

urlpatterns = [
    path('', view=home),
    path('about', view=about),
    path('menu', view=menu),
    path('book', view=book),
]