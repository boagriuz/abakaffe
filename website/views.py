from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
from models import CoffeeBrewer




# Create your views here.
def brewer_post(request):
	if request.method == 'POST':
		add_brewer(request.data)
	elif request.method == 'GET':
		#Fetching RFID from request
		s = request.META['QUERY_STRING']
		return checkRFID(s)

	#return HttpResponse("mjau")

def checkRFID(ID):
	entry = CoffeeBrewer.objects.filter(RFID = ID)
	response = HttpResponse()
	if entry.exists():
		response.content = True
	else:
		response.content = False
	return response

def add_brewer(data):
	brewer = CoffeeBrewer(datetime = datetime.now(), RFID = data['RFID'], name = data['name'])
	brewer.save()
