from django.urls import path
from .views import home, drinks

urlpatterns = [
    path('test', view=home, name="home"),
    path('drinks/<str:drink_name>', view=drinks, name="drinks")
]