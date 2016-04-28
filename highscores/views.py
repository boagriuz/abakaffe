from django.shortcuts import render
import datetime
from models import Brews
import operator
from update.models import CoffeeBrewer
from django.utils import simplejson


def view(request):
    monthly = simplejson.dumps(get_monthly_highscore())
   	alltime = simplejson.dumps(get_alltime_highscore())
    return render_template_to_response("highscore.html", {"monthly": monthly, "alltime": alltime})



def get_monthly_highscore():
	start_date = datetime.datetime.now() - datetime.timedelta(30)
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
		ID = entry.RFID
		name = CoffeeBrewer.objects.values_list("name", flat=True).filter(RFID = ID)[0]
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





