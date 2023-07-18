from rest_framework.generics import ListAPIView
from .serializers import BookListSerilizers
from book.models import Book

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerilizers