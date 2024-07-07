from django.shortcuts import render
from .serializers import BookApi
from .models import Books
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# class BookListApi(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookApi

class BookListApi(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BookApi(books, many=True).data
        data = {
            "books": serializer
        }
        return Response(data, status=200)


# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookApi

class BookDetailApi(APIView):
    def get(self, request, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BookApi(book).data
            return Response({'data':serializer},  status=status.HTTP_200_OK)
        except Books.DoesNotExist:
            return Response(
                {
                  "message":False,
                  "description":"invalid PK"
                 }, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "message": False,
                    "description": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
# class BookUpdateApi(generics.UpdateAPIView):
#     querysert =Books.objects.all()
#     serializer_class = BookApi

class BookUpdateApi(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Books.objects.all(), id=pk)
        data = request.data
        serializer = BookApi(instance=book, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            context = {
            'status':200,
            "message":f'{book} succesfully updated',
            'book':serializer.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        elif Exception:
            return Response({'status':False, "message":f'{Exception} xatoligi mavjud'}, status=status.HTTP_400_BAD_REQUEST)

# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookApi

class BookDeleteApi(APIView):
    def delete(self, request, pk):
        try: 
           book = Books.objects.get(id=pk)
           book.delete()
           return Response({"status":True, 'message':"Succesfully deleted"}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'status':False, 'message':f'have {error} error'})
            

# class BookCreate(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookApi

class BookCreate(APIView):
    def post(self, request):
        data = request.data
        serializer = BookApi(data=data)
        if serializer.is_valid():
            serializer.save()
            context = { 
                "message":True,
                "data":data,
            }
            return Response(context, status=status.HTTP_200_OK)

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