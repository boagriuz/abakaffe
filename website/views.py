from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from .models import CoffeeBrewer





@csrf_exempt
def brewer_post(request):
	response = HttpResponse()
	if request.method == 'POST':
		ID = request.POST.get('RFID')
		#Check if card is already registered
		s = RFID_in_DB(ID)
		print s
		if not s:
			add_brewer(request.POST)
			print("Added user to DB")
		else:
			print("User already in DB")
		return HttpResponse()


	elif request.method == 'GET':
		ID = request.META['QUERY_STRING']
		#Fetching RFID from request
		response.content = RFID_in_DB(ID)
	return response


def RFID_in_DB(ID):
	entry = CoffeeBrewer.objects.filter(RFID = ID)
	return entry.exists()
	


def add_brewer(data):
	brewer = CoffeeBrewer(datetime = datetime.datetime.now(), RFID = data.get('RFID'), name = data.get('name'))
	brewer.save()
