from rest_framework.generics import ListAPIView , GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from .serializers import  UserListSerilizer , UserRegisterSerilizer , ChangePasswordSerialier
from .custom_permissions import IsNotAuthenticated


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerilizer

class UserRegistration(GenericAPIView):
    serializer_class = UserRegisterSerilizer
    permission_classes = [IsNotAuthenticated]

    def post(self,request,*args,**kwargs):
        serilizer = self.serializer_class(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            email = serilizer.validated_data['email']
            return Response(f'create {email} account',status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordApiView(APIView):
    model = User
    serializer_class = ChangePasswordSerialier

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


    

