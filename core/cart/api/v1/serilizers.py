from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from book.models import Book
from cart.models import OrderDetail , Order

class AddToCartSerlizer(serializers.Serializer):
    id = serializers.CharField()
    count = serializers.IntegerField(min_value=0)

    def validate(self, attrs):
        id = attrs.get('id')
        count = attrs.get('count')

        book = Book.objects.filter(id=id).last()
        if book is None:
            raise ValidationError("book does not exist.")
        
        if count > book.cover_count:
            raise ValidationError("error, too much count.")

        return attrs

class RemoveFromCartSerlizer(serializers.Serializer):
    id = serializers.CharField()

    def validate(self, attrs):
        id = attrs.get('id')
        request = self.context.get('request', None)
        orderdetail = OrderDetail.objects.filter(id=id).last()

        if orderdetail is None:
            raise ValidationError("orderdetail does not exist.")
        
        if orderdetail.order.owner != request.user:
            raise ValidationError("you cant delete this orderdetail.")

        return attrs

# class OrderDetailSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDetail
#         fields = '__all__'


# class OpenCartSerilizer(serializers.Serializer):
#     class Meta:
#         model = Order
#         fields = ('owner','')
