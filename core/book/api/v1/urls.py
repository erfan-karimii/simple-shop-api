from django.urls import path 
from . import views

app_name = "api-v1"

urlpatterns = [
    path('book-list/',views.BookList.as_view(),name='book-list'),
    path('book-detail/<pk>/',views.BookDetail.as_view(),name='book-detail'),
    path('author-detail/<pk>/',views.AuthorDetail.as_view({'get': 'retrieve'}),name='author-detail'),
    path('category-detail/<pk>/',views.CategoryDetail.as_view({'get': 'retrieve'}),name='category-detail'),
    path('booktags-detail/<pk>/',views.BookTagsDetail.as_view({'get': 'retrieve'}),name='booktags-detail'),
]

