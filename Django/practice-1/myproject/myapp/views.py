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

def menu(request):
    return HttpResponse("This is menu view")

def about(request):
    about_content = {
        'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
        } 

    return render(request, 'about.html', {'content': about_content})