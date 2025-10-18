from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Little Lemon</h1>")

def drinks(request, drink_name):
    drinks = {
        "mocha": "type of coffee",
        "tea": "type of beverage",
        "lemonade": "type of refreshment"
    }

    choice_of_drink = drink_name