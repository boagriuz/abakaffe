from django.shortcuts import render
import datetime
from models import Brews
import operator


# Create your views here.

def get_monthly_highscore():
	start_date = datetime.datetime.now() - datetime.timedelta(-30)
	entries = Brews.objects.filter(dateTime__gt = start_date)
	scores = get_scores(entries)
	highscores = get_top_10(scores)
	return higschores



#Takes a queryset and returns a dictionary containing the number of brews for each RFID in the set
def get_scores(queryset):
	scores = {}
	for entry in entries:
		ID = entry.RFID
		if ID in scores.keys():
			scores[ID] += 1
		else:
			scores[ID] = 1
	return scores



def get_alltime_highscore():
	entries = Brews.objects.all()
	scores = get_scores(entries)
	highscores = get_top_10(scores)
	return highscores



#Takes a dictionary and returns top 10 as a list of tuples
def get_top_10(scores):#scores must be a dict
	top_scores = sorted(scores.items(), key=operator.itemgetter(1))
	global top_scores
	top_scores.reverse()
	return topscores[:10]
