from django.urls import path 
from . import views

app_name = 'api-v1'


urlpatterns = [
    path('checkout/',views.checkout,name="checkout"),
    path('orders/', views.OrdersList.as_view(),name='orders'),  
]
