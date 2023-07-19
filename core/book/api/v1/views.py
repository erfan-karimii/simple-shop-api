from rest_framework.generics import ListAPIView ,RetrieveAPIView
from rest_framework import viewsets
from .serializers import BookListSerilizers , BookDetailSerilizers , AuthorSerilizers , CategorySerilizers , BookTagsSerilizers
from book.models import Book , Author , Category , BookTags

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerilizers

class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerilizers

class AuthorDetail(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizers

class CategoryDetail(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizers

class BookTagsDetail(viewsets.ModelViewSet):
    queryset = BookTags.objects.all()
    serializer_class = BookTagsSerilizers