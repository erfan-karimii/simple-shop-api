from rest_framework import serializers
from book.models import Book , Category , BookTags , Author

class BookListSerilizers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        exclude = ('info','is_active')
        extra_kwargs = {
            'url': {'view_name': 'book:api-v1:book-detail'},
            'author': {'view_name': 'book:api-v1:author-detail'},
            'category': {'view_name': 'book:api-v1:category-detail'},
            'tags': {'view_name': 'book:api-v1:booktags-detail'},
        }

class BookDetailSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    


class CategorySerilizers(serializers.ModelSerializer):
    related_book_count = serializers.IntegerField(source='get_related_book_count',read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
    

class AuthorSerilizers(serializers.ModelSerializer):
    author_book_count = serializers.IntegerField(source='get_author_book_count',read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

class BookTagsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = BookTags
        fields = '__all__'