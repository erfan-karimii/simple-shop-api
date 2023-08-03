from rest_framework.generics import GenericAPIView , RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddToCartSerlizer , RemoveFromCartSerlizer , OpenCartSerilizer ,OrderDetailSerilizer
from cart.models import Order , OrderDetail

class AddToCart(GenericAPIView):
    serializer_class = AddToCartSerlizer
    def get(self,request,*args,**kwargs):
        serilizer = self.serializer_class(data=request.data)
        if serilizer.is_valid():
            id = serilizer.validated_data['id']
            count = serilizer.validated_data['count']
            order = Order.objects.filter(owner=request.user,is_paid=False).last()
            if order is None:
                order = Order.objects.create(owner=request.user)
                order.orderdetail_set.create(book_id=id,orderdetail_count=count)
            else:
                order.orderdetail_set.update_or_create(book_id=id,defaults={'orderdetail_count':count})
            return Response({'added':'True'},status=status.HTTP_200_OK)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RemoveFromCart(GenericAPIView):
    serializer_class = RemoveFromCartSerlizer
    def get(self,request,*args,**kwargs):
        serilizer = self.get_serializer(data=request.data)
        if serilizer.is_valid():
            id = serilizer.validated_data['id']
            OrderDetail.objects.get(id=id).delete()
            return Response({'removed':'True'},status=status.HTTP_200_OK)
        else:
            return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)


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

