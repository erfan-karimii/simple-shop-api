from django.contrib import admin
from .models import Author , Book , BookTags , Category

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookTags)
admin.site.register(Category)
