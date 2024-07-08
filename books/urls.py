from django.urls import path
from .views import BookListApi, books_list, BookUpdateApi, BookDeleteApi, BookDetailApi, BookViewSet
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("books", BookViewSet, basename='books')

urlpatterns = [
    path('', BookListApi.as_view()),
    # path('books/', books_list),
    # path('books/create', views.BookCreate.as_view()),
    # path('books/<int:pk>/dud/', views.BookDUD.as_view()),
    # path('books/<int:pk>/', BookDetailApi.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApi.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApi.as_view()),
]
urlpatterns = urlpatterns + router.urls