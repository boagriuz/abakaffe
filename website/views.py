from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import CoffeeBrewer

@csrf_exempt
def brewer_post(request):
	response = HttpResponse()
	if request.method == 'POST':
		ID = request.POST.get('RFID')
		name = request.POST.get('NAME')
		#Check if card is already registered
		s = RFID_in_DB(ID)
		if not s:
			print(request.POST)
			add_brewer(request.POST)
			print("Added user to DB")
		else:
			print("User already in DB")
		return HttpResponse()

	elif request.method == 'GET':
		ID = request.META['QUERY_STRING']
		#Fetching RFID from request
		response.content = RFID_in_DB(ID)
		if response.content:
			entry = CoffeeBrewer.objects.get(RFID = ID)
			entry.brews += 1
			print(entry.brews)
			entry.save()
	return response

def RFID_in_DB(ID):
	entry = CoffeeBrewer.objects.filter(RFID = ID)
	return entry.exists()

def add_brewer(data):
	brewer = CoffeeBrewer(datetime = timezone.now(), RFID = data.get('RFID'), name = data.get('NAME'))
	brewer.save()
