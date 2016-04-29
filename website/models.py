from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Subscribe(models.Model):
    studmail = models.TextField(primary_key=True, max_length=20, default=0)
    created = models.TextField(max_length=10, default=0)

'''
# use case 1:
1. bruker taster inn email
2. trykker subscribe (gjelder for de neste 24 timer)
3. studmail legges til tabell Subscribe i db
4. en notify email blir sendt

#use case 2:
1. bruker taster inn email og trykker Unsubscribe
2. bruker studmail blir slettet fra db

#use case 3:
1. bruker trykker pa unsubscribe link i mottatt notify mail
2. email slettes fra tabell Subscribe i db
'''
