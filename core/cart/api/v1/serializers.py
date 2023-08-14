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

class OrderDetailSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'cart:api-v1:cart-detail'},
            'order': {'view_name': 'cart:api-v1:open-cart'},
            'tags': {'view_name': 'book:api-v1:book-detail'},
        }


class OpenCartSerilizer(serializers.ModelSerializer):
    related_orderdetail = serializers.SerializerMethodField()

    def get_related_orderdetail(self,obj):
        related_detail = obj.orderdetail_set.all()
        serializer = OrderDetailSerilizer(related_detail,many=True,context={"request":self.context.get('request')})
        return serializer.data
     
    class Meta:
        model = Order
        # fields = ('owner','is_paid','related_orderdetail','first_name',
        #         'last_name','address','phone_number','paid_amout','strip_token')
        exclude = ('payment_date',)
    
    def create(self, validated_data):
        items_data = validated_data.pop('related_detail')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderDetail.objects.create(order=order,**item)
             
        return order