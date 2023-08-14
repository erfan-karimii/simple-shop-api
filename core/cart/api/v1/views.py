import stripe

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render

from rest_framework.generics import GenericAPIView , RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework import status , authentication ,permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import AddToCartSerlizer , RemoveFromCartSerlizer , OpenCartSerilizer ,OrderDetailSerilizer
from cart.models import Order , OrderDetail

User = get_user_model()

class OrderDetailView(RetrieveAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerilizer


class OpenOrder(GenericAPIView):
    serializer_class = OpenCartSerilizer
    def get(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return Response({'not allowed':'please login or sign-up '},status=status.HTTP_401_UNAUTHORIZED)

        order , created = Order.objects.get_or_create(owner=request.user)
        if created or not order.orderdetail_set.all().exists():
            return Response({'cart is empty':'your cart is empty , please visite other pages to add product'},status.HTTP_200_OK)
        
        serilizer = self.get_serializer(order)
        return Response(serilizer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes(permissions.IsAuthenticated)
def checkout(request):
    serilizer = OrderDetailSerilizer(data=request.data)
    if serilizer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') for item in serilizer.validated_data['items'])

        try:
            charg = stripe.Charge.create(
                amount= int(paid_amount*100),
                currency = 'USD',
                description = 'charg from book_store',
                source = serilizer.validated_data['stripe_token']
            )
            serilizer.save(user=request.user,paid_amount=paid_amount)
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

# class AddToCart(GenericAPIView):
#     serializer_class = AddToCartSerlizer
#     def get(self,request,*args,**kwargs):
#         serilizer = self.serializer_class(data=request.data)
#         if serilizer.is_valid():
#             id = serilizer.validated_data['id']
#             count = serilizer.validated_data['count']
#             order = Order.objects.filter(owner=request.user,is_paid=False).last()
#             if order is None:
#                 order = Order.objects.create(owner=request.user)
#                 order.orderdetail_set.create(book_id=id,quantity=count)
#             else:
#                 order.orderdetail_set.update_or_create(book_id=id,defaults={'quantity':count})
#             return Response({'added':'True'},status=status.HTTP_200_OK)
#         else:
#             return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

# class RemoveFromCart(GenericAPIView):
#     serializer_class = RemoveFromCartSerlizer
#     def get(self,request,*args,**kwargs):
#         serilizer = self.get_serializer(data=request.data)
#         if serilizer.is_valid():
#             id = serilizer.validated_data['id']
#             OrderDetail.objects.get(id=id).delete()
#             return Response({'removed':'True'},status=status.HTTP_200_OK)
#         else:
#             return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)