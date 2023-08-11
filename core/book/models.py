from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator


from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class BookTags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    language_choices = (
        ('fa','farsi'),
        ('en','english'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True,blank=True)
    image = models.ImageField()
    thumbnail = models.ImageField(null=True,blank=True)
    alt = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name='قیمت اصلی')
    discount_percentage = models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)],verbose_name='درصد تخفیف')
    cover_count = models.PositiveBigIntegerField(verbose_name='تعداد محصول',validators=[MinValueValidator(0)])
    author = models.ForeignKey('Author',on_delete=models.PROTECT)
    category = models.ForeignKey('Category',on_delete=models.PROTECT,null=True,related_name='books')
    description = models.TextField(null=True,verbose_name='توضیح کوتاه')
    info = RichTextUploadingField()
    tags = models.ManyToManyField('BookTags')
    book_language = models.CharField(max_length=2,choices=language_choices,default='fa')
    published_date = models.DateField(null=True)
    created  =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def main_discount_call(self):
        return self.price - (self.price * (self.discount_percentage/100))
    
    def save(self,*args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        super().save()



    def make_thumbnail(self,image,size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail = File(thumb_io,name=image.name)
        return thumbnail



class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام دسته بندی')
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    
    def get_related_book_count(self):
        count = self.books.count()
        return count

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.full_name
    
    def get_author_book_count(self):
        count = self.books.count()
        return count