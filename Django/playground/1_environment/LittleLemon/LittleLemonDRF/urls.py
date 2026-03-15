from django.urls import path
from .views import SingleMenuItemView, MenuItemView

urlpatterns = [
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view())
]