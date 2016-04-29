from django.test import TestCase
from highscores.models import Brews
from update.models import CoffeeBrewer
from django.utils import timezone
from highscores.views import get_monthly_highscore, get_alltime_highscore
import datetime

# Create your tests here.


class BrewerTestCase(TestCase):
	a = None
	b = None
	c = None
	d = None
	def setUp(self):
		self.a = CoffeeBrewer.objects.create(datetime = timezone.now(), RFID = '1111', name = 'Anders')
		self.b = CoffeeBrewer.objects.create(datetime = timezone.now(), RFID = '1112', name = 'Alexander')
		self.c = CoffeeBrewer.objects.create(datetime = timezone.now(), RFID = '1113', name = 'Magnus')
		self.d = CoffeeBrewer.objects.create(datetime = timezone.now(), RFID = '1114', name = 'Even')
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1111'), dateTime = datetime.datetime.now())
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1111'), dateTime = datetime.datetime(2016, 4, 24, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1111'), dateTime = datetime.datetime(2016, 4, 22, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1112'), dateTime = datetime.datetime(2016, 4, 13, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1112'), dateTime = datetime.datetime(2016, 4, 21, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1113'), dateTime = datetime.datetime(2016, 4, 17, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1114'), dateTime = datetime.datetime(2015, 4, 24, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1114'), dateTime = datetime.datetime(2015, 4, 22, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1114'), dateTime = datetime.datetime(2015, 4, 13, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1114'), dateTime = datetime.datetime(2015, 4, 21, 19, 45, 30, 4))
		Brews.objects.create(RFID = CoffeeBrewer.objects.get(RFID='1114'), dateTime = datetime.datetime(2015, 4, 17, 19, 45, 30, 4))


	def test_monthly_highscores(self):
		self.assertEqual(get_monthly_highscore(), [('Anders', 3), ('Alexander', 2), ('Magnus', 1)])


	def test_get_alltime_highscore(self):
		self.assertEqual(get_alltime_highscore(), [('Even', 5), ('Anders', 3), ('Alexander', 2), ('Magnus', 1)])

