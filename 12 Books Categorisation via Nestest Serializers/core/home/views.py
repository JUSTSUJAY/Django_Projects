from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def get_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({'status':200, 'payload':serializer.data})

# Create your views here.
