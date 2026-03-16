from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def book(request):
    if request.method == 'GET':
        books = Book.objects.all().values
        return JsonResponse({'books': books})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book = Book(
            title = title,
            author = author,
            price = price
        )

        try:
            book.save()
        except IntegrityError as ICE:
            return JsonResponse({'error': True, 'message': 'required field missing'},
                                status=400)
        return JsonResponse(model_to_dict(book), 201)