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
    first_name = models.CharField(max_length=250,null=True,blank=True)
    last_name = models.CharField(max_length=250,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=15,validators=[validate_phone_number],null=True,blank=True)
    paid_amount = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    is_paid = models.BooleanField(default=False)
    stripe_token = models.CharField(max_length=100,null=True,blank=True)
    payment_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return str(self.owner) + " ////////// " + str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order.id) + " ////////// " + str(self.book.title)
