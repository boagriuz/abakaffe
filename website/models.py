from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CoffeeBrewer(models.Model):
	datetime = models.DateTimeField()
	RFID = models.CharField(max_length=10)
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.RFID

