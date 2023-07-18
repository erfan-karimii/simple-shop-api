from rest_framework.generics import ListAPIView , CreateAPIView
from rest_framework.permissions import IsAuthenticated 
from account.models import User
from .serializers import  UserListSerilizers , UserRegisterSerilizers


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerilizers
    permission_classes = [IsAuthenticated]

class RegisterUser(CreateAPIView):
    serializer_class = UserRegisterSerilizers
    

