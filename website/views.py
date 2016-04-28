from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from update.models import Weight
from highscores.views import view

def index(request, template = "website/index.html"):
    context = {'WEIGHT' : Weight.objects.get(pk=1).weight}
    return render(request, template, context)

def highscore(request, template = "website/highscore.html"):
    context = view(request)
    return render(request, template, context)

def about(request, template = "website/about.html"):
    return render(request, template)
