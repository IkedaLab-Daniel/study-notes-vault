from django.urls import path
from .views import form_view

urlpatterns = [
    path('', view=form_view, name="form_view"),
]