from django.shortcuts import render
from .serializers import BookApi
from .models import Books
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class BookListApi(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookApi

class BookDetailApi(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookApi

class BookUpdateApi(generics.UpdateAPIView):
    querysert =Books.objects.all()
    serializer_class = BookApi

class BookDeleteApi(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookApi

class BookCreate(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookApi

class BookLC(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookApi

class BookDUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookApi

# ListApiView with function.
@api_view(['GET'])
def books_list(request):
    book = Books.objects.all()
    serializer = BookApi(book, many=True)
    return Response(serializer.data)