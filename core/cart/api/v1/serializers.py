from rest_framework import serializers
from book.api.v1.serializers import BookDetailSerilizers
from cart.models import OrderItem , Order

class MyOrderItemSerializer(serializers.ModelSerializer):    
    book = BookDetailSerilizers()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "book",
            "quantity",
            'book'
        )

class MyOrderSerializer(serializers.ModelSerializer):
    orderitem_set = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = ('payment_date','owner')

class OrderItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('price','book','quantity')

class CartSerilizer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerilizer(many=True)
     
    class Meta:
        model = Order
        exclude = ('payment_date','owner')
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order,**item)

        return order
