from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Menu

# Create your views here.
def menu(request):
    menu_items = Menu.objects.all()
    item_dict = {
        "menu": menu_items
    }

    return render(request, "menu.html", item_dict)