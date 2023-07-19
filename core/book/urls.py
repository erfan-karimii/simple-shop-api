from django.urls import path , include
from book.api.v1 import views
app_name = 'book'


urlpatterns = [
    path('api/v1/',include('book.api.v1.urls')),
    
]
