from django.urls import path 
from . import views

app_name = 'api-v1'


urlpatterns = [
    path('add-to-cart/',views.AddToCart.as_view(),name="add-to-cart"),
    path('remove-from-cart/',views.RemoveFromCart.as_view(),name="remove-from-cart"),

]
