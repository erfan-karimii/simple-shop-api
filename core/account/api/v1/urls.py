from django.urls import path 
from . import views

urlpatterns = [
    path('user-list/',views.UserListView.as_view()),
    path('user-registration/',views.UserRegistration.as_view())
]
