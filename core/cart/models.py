from django.db import models
from book.models import Book
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re
# Create your models here.

MyUser = get_user_model()

def validate_phone_number(value):
    if  not bool(re.compile("^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$").match(value)):
        raise ValidationError(
            _('number is not valid'),
        )

class Order(models.Model):
    owner = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    address = models.TextField()
    phone_number = models.CharField(max_length=15,validators=[validate_phone_number])
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField()

    def get_total_price(self):
        amount = 0 
        for detail in self.orderdetail_set.all():
            amount += detail.book.price * detail.orderdetail_count

        return amount

    def __str__(self):
        return str(self.id) + " " + str(self.owner)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    orderdetail_count = models.IntegerField()

    def get_detail_sum(self):
        return self.orderdetail_count * self.book.price

    def __str__(self):
        return str(self.order) + " " + str(self.book)
