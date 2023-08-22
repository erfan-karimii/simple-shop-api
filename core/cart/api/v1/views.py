import stripe

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework import status  ,permissions 

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import CartSerilizer ,MyOrderSerializer
from cart.models import Order

User = get_user_model()

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serilizer = CartSerilizer(data=request.data)
    if serilizer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') for item in serilizer.validated_data['orderitem_set'])

        try:
            charg = stripe.Charge.create(
                amount= int(paid_amount*100),
                currency = 'USD',
                description = 'charg from book_store',
                source = serilizer.validated_data['stripe_token']
            )
            serilizer.save(owner=request.user,paid_amount=paid_amount)
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

    return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrdersList(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(owner=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

