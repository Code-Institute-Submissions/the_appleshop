from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone


class Review(models.Model):

    title = models.CharField(max_length=254, default='')
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    view_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title