from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import CoffeeBrewer


def index(request):
	template = loader.get_template("website/index.html")
	# context = {'something' : something}
	return HttpResponse(template.render())



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
			#entry = CoffeeBrewer.objects.get(RFID = ID)
			#entry.brews += 1
			add_brew(ID)
			#print(entry.brews)
			#entry.save()
	return response

def RFID_in_DB(ID):
	entry = CoffeeBrewer.objects.filter(RFID = ID)
	return entry.exists()


def add_brew(RFID):
	brew = Brew(datetime = timezone.now(), RFID = RFID)
	brew.save()

def add_brewer(data):
	brewer = CoffeeBrewer(datetime = timezone.now(), RFID = data.get('RFID'), name = data.get('NAME'))
	brewer.save()
