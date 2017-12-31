from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


categories = [
        (1, 'Books'),
        (2, 'Vehicle'),
    ]

# Create your models here.
class Advertisment(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	category = models.IntegerField(categories)
	description = models.CharField(max_length=500)
	mobileNumber = models.BigIntegerField()
	address = models.CharField(max_length=250)




