from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام دسته بندی')

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.full_name

class BookTags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    alt = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name='قیمت اصلی')
    discount_percentage = models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)],verbose_name='درصد تخفیف')
    book_count = models.PositiveBigIntegerField(verbose_name='تعداد محصول',validators=[MinValueValidator(0)])
    author = models.ForeignKey(Author,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    info = RichTextField()
    tags = models.ManyToManyField(BookTags)
    created  =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def main_discount_call(self):
        return self.price - (self.price * (self.discount_percentage/100))