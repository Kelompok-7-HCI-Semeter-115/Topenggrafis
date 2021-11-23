from django.db import models
from django import forms

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=12)
    CHOICES = (('Option 1', 'Graphic Design'),('Option 2', 'Photography'),('Option 3', 'Art Project'))
    services = models.CharField(choices=CHOICES,max_length=200)

    def __str__(self):
        return "{}.{}".format(self.id,self.full_name)
    