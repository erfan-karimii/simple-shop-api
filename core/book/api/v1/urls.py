from django.urls import path 
from rest_framework import routers
from . import views

app_name = "api-v1"

router = routers.DefaultRouter()

router.register(r'author', views.AuthorViewset)
router.register(r'category', views.CategoryViewset)
router.register(r'booktags', views.BookTagsViewset)


urlpatterns = [
    path('book-list/',views.BookList.as_view(),name='book-list'),
    path('book-detail/<pk>/',views.BookDetail.as_view(),name='book-detail'),
]

urlpatterns += router.urls