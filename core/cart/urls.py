from django.urls import path , include
from book.api.v1 import views

app_name = 'cart'


urlpatterns = [
    path('api/v1/',include('cart.api.v1.urls')),   
]
