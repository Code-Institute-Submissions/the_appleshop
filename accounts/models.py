from django.db import models
from django.contrib.auth.models import User


class UserAddress(models.Model):
    user = models.ForeignKey(User, null=False)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False) 
    county = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return self.full_name

