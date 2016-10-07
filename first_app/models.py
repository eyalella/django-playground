from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Apartment(models.Model):
  user = models.ForeignKey(User)
  size = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  location = models.CharField(max_length=100)
  image = models.ImageField(default='default.jpg')

  def __str__(self):
    return self.location
