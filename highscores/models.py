from __future__ import unicode_literals
from django.
from django.db import models

# Create your models here.

class Brews(models.Model):
	datetime = models.DateTimeField()
	RFID = models.ForeignKey('website.CoffeeBrewer')
