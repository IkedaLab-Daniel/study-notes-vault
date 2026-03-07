from django.shortcuts import render
from myapp.forms import BookingForm

# Create your views here.
def form_view(request):
   form = BookingForm()
   if request.method == 'POST':
      form = BookingForm(request.POST)
      if form.is_valid():
         form.save()
   
   context = {"form": form}
   return render(request, "booking.html", context)