from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Subscribe(models.Model):
    studmail = models.TextField(primary_key=True, max_length=20, unique=True, default=0)
    created = models.BigIntegerField(default=0)
