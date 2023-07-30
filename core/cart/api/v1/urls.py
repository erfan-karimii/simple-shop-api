from django.urls import path 
from . import views

app_name = 'api-v1'


urlpatterns = [
    path('add-to-cart/',views.AddToCart.as_view(),name="add-to-cart"),
    path('cart-detail/<id>/',views.OrderDetailView.as_view(),name="cart-detail"),
    path('remove-from-cart/',views.RemoveFromCart.as_view(),name="remove-from-cart"),
    path('open-cart/',views.OpenOrder.as_view(),name="open-cart"),
]
