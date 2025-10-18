from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drinks(request, drink_name):
    drink = {
        "mocha": "type of coffee",
        "tea": "type of beverage",
        "lemonade": "type of refresehment",
    }

    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)