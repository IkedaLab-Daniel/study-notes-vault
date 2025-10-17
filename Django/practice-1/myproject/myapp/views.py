from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm

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

    return HttpResponse(f"<h2>{drink_name} </h2>" + drinks[drink_name])

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "myapp/booking.html", context)