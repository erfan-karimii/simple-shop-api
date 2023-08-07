from rest_framework.generics import ListCreateAPIView ,RetrieveAPIView
from rest_framework import viewsets
from rest_framework import filters
# from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BookListSerilizers , BookDetailSerilizers , AuthorSerilizers , CategorySerilizers , BookTagsSerilizers
from .pagination import LargeResultsSetPagination
from book.models import Book , Author , Category , BookTags

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    # pagination_class = LargeResultsSetPagination
    serializer_class = BookListSerilizers
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title','category__name']
    ordering_fields = ['title', 'published_date','price']

class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerilizers

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizers

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizers


class BookTagsViewset(viewsets.ModelViewSet):
    queryset = BookTags.objects.all()
    serializer_class = BookTagsSerilizers