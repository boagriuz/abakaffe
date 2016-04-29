from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import Brews
import operator
from update.models import CoffeeBrewer
import json

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_monthly_alltime():
    monthly = get_monthly_highscore()
    alltime = get_alltime_highscore()
    return monthly, alltime


def get_statistics():
    stat = statistics()
    return stat


# Creates statistics of the last seven days, returns number og brews for each weekday
def statistics():
    start_date = timezone.now() - datetime.timedelta(7)
    entries = Brews.objects.filter(dateTime__gt=start_date)
    stati = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for entry in entries:
        day = entry.dateTime.weekday()
        if day in stati:
            stati[day] += 1
    return sort_statistics(stati)


def get_monthly_highscore():
    start_date = timezone.now() - datetime.timedelta(30)
    entries = Brews.objects.filter(dateTime__gt=start_date)
    scores = get_scores(entries)
    highscores = get_top_10(scores)
    return highscores


def get_alltime_highscore():
    entries = Brews.objects.all()
    scores = get_scores(entries)
    highscores = get_top_10(scores)
    return highscores


# Takes a queryset and returns a dictionary containing the number of brews for each RFID in the set
def get_scores(queryset):
    scores = {}
    for entry in queryset:
        name = entry.RFID.name
        if name in scores.keys():
            scores[name] += 1
        else:
            scores[name] = 1
    return scores


# Takes a dictionary and returns top 10 as a list of tuples
def get_top_10(scores):  # scores must be a dict
    top_scores = sorted(scores.items(), key=operator.itemgetter(1))
    top_scores.reverse()
    return top_scores[:10]


# Sortes statistics and places this weekday's values first.
def sort_statistics(stati):
    sorted_stat = []
    today = timezone.now().weekday()
    for i in range(today + 1, today + 8):
        if i > 6:
            sorted_stat.append((days[i - 7], stati[i - 7]))
        else:
            sorted_stat.append((days[i], stati[i]))

    return sorted_stat
