from django.http import HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("Welcome")

def menu(request):
   return HttpResponse("Menu")

def about(request):
   return HttpResponse("About Us")

def book(request):
   return HttpResponse("Make a booking")