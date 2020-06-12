from django.db import models
from django.contrib.auth.models import User


class Wishlist(models.Model):
    name = models.CharField(max_length=254, default='')
    user = models.ForeignKey(User, null=False)
    products = models.CommaSeparatedIntegerField(max_length=254, default='')

    def __str__(self):
        return self.name