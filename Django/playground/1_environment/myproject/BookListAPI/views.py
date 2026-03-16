from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        author = data.get('author')
        price = data.get('price')

        book = Book(
            title = title,
            author = author,
            price = price
        )

        try:
            book.save()
        except IntegrityError as ICE:
            return JsonResponse({'error': 'true', 'message': 'required field missing'},
                                status=400)
        return JsonResponse(model_to_dict(book), status=201)