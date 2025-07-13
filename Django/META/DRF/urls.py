from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books),
    path('classbooks/', views.BookList.as_view()),
    path('classbooks/<int:pk>', views.Book.as_view())
]