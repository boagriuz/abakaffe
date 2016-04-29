from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import Brews
import operator
from update.models import CoffeeBrewer
import json


def get_monthly_alltime():
	monthly = get_monthly_highscore()
	alltime = get_alltime_highscore()
	return monthly, alltime


def get_statistics():
	stat = statistics()
	return stat


#Creates statistics of the last seven days, returns number og brews for each weekday
def statistics():
	start_date = timezone.now() - datetime.timedelta(7)
	entries = Brews.objects.filter(dateTime__gt = start_date)
	stat = {}
	for entry in entries:
		day = entry.dateTime.weekday()
		if day in stat:
			stat[day] += 1
		else:
			stat[day] = 1
	return stat



def get_monthly_highscore():
	start_date = timezone.now() - datetime.timedelta(30)
	entries = Brews.objects.filter(dateTime__gt = start_date)
	scores = get_scores(entries)
	highscores = get_top_10(scores)
	return highscores



def get_alltime_highscore():
	entries = Brews.objects.all()
	scores = get_scores(entries)
	highscores = get_top_10(scores)
	return highscores



#Takes a queryset and returns a dictionary containing the number of brews for each RFID in the set
def get_scores(queryset):
	scores = {}
	for entry in queryset:
		name = entry.RFID.name
		if name in scores.keys():
			scores[name] += 1
		else:
			scores[name] = 1
	return scores



#Takes a dictionary and returns top 10 as a list of tuples
def get_top_10(scores):#scores must be a dict
	top_scores = sorted(scores.items(), key=operator.itemgetter(1))
	top_scores.reverse()
	return top_scores[:10]





