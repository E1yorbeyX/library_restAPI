from .models import Books
from rest_framework import serializers


class BookApi(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'description', 'isbn', 'author', 'price']