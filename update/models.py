from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CoffeeBrewer(models.Model):
	datetime = models.DateTimeField()
	RFID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.RFID


class Weight(models.Model):
	weight = models.IntegerField(default=0)
	key = models.IntegerField(default=1)
