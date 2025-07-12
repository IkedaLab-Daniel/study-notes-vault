from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hello_world),
    path('books/', views.books)
]