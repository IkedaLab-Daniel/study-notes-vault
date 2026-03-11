from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def menu(request):
    return render(request, "menu")

def about(request):
    return render(request, "request")

def book(request):
    return render(request, "book")
