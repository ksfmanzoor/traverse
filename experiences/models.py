from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from places.models import Place
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    image = models.ImageField(null=True, upload_to='experience_images/category_covers')

    def __str__(self):
        return self.title


class Experience (models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256, unique=True)
    content = models.TextField()
    date_booked = models.DateTimeField(default=timezone.now, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True, upload_to='experience_images')
    location = models.ForeignKey(Place, on_delete=models.PROTECT)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
