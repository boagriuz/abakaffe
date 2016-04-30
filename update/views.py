from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import CoffeeBrewer
from .models import Weight
from highscores.models import Brews


@csrf_exempt
def brewer_post(request):
    response = HttpResponse()
    if request.method == 'POST':
        ID = request.POST.get('RFID')
        brew = request.POST.get('BREW')
        name = request.POST.get('NAME')
        temp_weight = request.POST.get('WEIGHT')
        # Checks what to do
        if temp_weight:
            create_weight_object(temp_weight)
        elif brew:
            # Adds a new Brew ot database
            add_brew(ID)
        elif name:
            # Adds a new CoffeeBrewer to database if ID doesn't already exist
            add_brewer(request.POST)
        return HttpResponse()
    elif request.method == 'GET':
        # Fetching RFID from request
        rfid = request.META['QUERY_STRING']
        try:
            #Check if RFID already in database
            response.content = RFID_in_DB(rfid)
        except ValueError:
            return response
    return response


def create_weight_object(temp_weight):
    print(temp_weight)
    entry = Weight.objects.get(key=1)
    entry.weight = temp_weight
    entry.save()


def add_brew(ID):
    if RFID_in_DB(ID):
        entry = Brews.objects.create(dateTime=timezone.now(), RFID=CoffeeBrewer.objects.get(RFID=ID))
        entry.save()
        print("Added brew to user: " + CoffeeBrewer.objects.get(RFID=ID).name)


def RFID_in_DB(ID):
    entry = CoffeeBrewer.objects.filter(RFID=ID)
    return entry.exists()


def add_brewer(data):
    print(data)
    if RFID_in_DB(data.get('RFID')):
        print("User already in database!")
    else:
        brewer = CoffeeBrewer(datetime=timezone.now(), RFID=data.get('RFID'), name=data.get('NAME'))
        brewer.save()
        print("Added user to DB")
