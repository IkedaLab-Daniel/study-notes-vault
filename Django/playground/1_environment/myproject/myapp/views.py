from django.http import HttpResponse
from django.shortcuts import render
# from .forms import BookingForm
from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def booking(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
    
#     content = {'form': form}
#     return render(request, 'book.html', context)