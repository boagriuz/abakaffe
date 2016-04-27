from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Brews(models.Model):
	dateTime = models.DateTimeField()
	RFID = models.ForeignKey('website.CoffeeBrewer')
