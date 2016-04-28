from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from update.models import Weight

def index(request, template = "website/index.html"):
    context = {'WEIGHT' : Weight.objects.get(pk=1).weight}
    return render(request, template, context)

def highscore(request):
    return render(request, "website/highscore.html")

def about(request):
    return render(request, "website/about.html")
