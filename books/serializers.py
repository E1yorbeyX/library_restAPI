from django.forms import ValidationError
from .models import Books
from rest_framework import serializers


class BookApi(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'description', 'isbn', 'author', 'price']
   
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise serializers.ValidationError(
             {"status":'Title must be alpha characters only'}
            )
        if Books.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                {"status":'Book already exists'} 
            )   
        return data

class Payme(serializers.Serializer):
    cardNumber = serializers.IntegerField()
    cardName = serializers.CharField(max_length=50) 
    cardExpire = serializers.CharField(max_length=5)