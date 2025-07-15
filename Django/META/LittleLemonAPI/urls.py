from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]