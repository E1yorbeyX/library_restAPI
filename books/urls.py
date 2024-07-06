from django.urls import path
from .views import BookListApi, books_list, BookUpdateApi, BookDeleteApi, BookDetailApi
from . import views

urlpatterns = [
    path('', BookListApi.as_view()),
    path('books/', books_list),
    path('books/create', views.BookCreate.as_view()),
    path('books/<int:pk>/dud/', views.BookDUD.as_view()),
    path('books/<int:pk>/', BookDetailApi.as_view()),
    path('books/<int:pk>/update/', BookUpdateApi.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApi.as_view()),
]