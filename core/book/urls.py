from django.urls import path , include

app_name = 'book'


urlpatterns = [
    path('api/v1/',include('book.api.v1.urls'))
]
