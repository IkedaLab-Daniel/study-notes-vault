from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('booking/', views.form_view), # > Lab 7
]