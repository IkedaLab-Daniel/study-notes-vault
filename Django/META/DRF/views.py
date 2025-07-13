from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        # ? URL Paramater
        author = request.GET.get('author')
        if (author):
            return Response({"message": "list of books by " + author}, status.HTTP_200_OK)

        return Response({"message":"list of the books"}, status.HTTP_200_OK)
    
    def post(self, request):
        # ? payload
        title = request.data.get('title')
        return Response({"message":"new book created: " + title}, status.HTTP_201_CREATED)
    
class Book(APIView):
    # ? primary key
    def get(self, request, pk):
        return Response({"message": "single book with id " + str(pk)}, status.HTTP_200_OK)

    def put(self, request, pk):
        title = request.data.get('title')
        return Response({"title": title}, status.HTTP_200_OK)
