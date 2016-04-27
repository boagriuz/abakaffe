from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import CoffeeBrewer
from update.views import weight
from django.shortcuts import render_to_response

def index(request):
    print(request)
    template = loader.get_template("website/index.html")
    context = {'WEIGHT' : weight}
    return render_to_response(template, context)

def highscore(request):
    return render(request, "website/highscore.html")

def about(request):
    return render(request, "website/about.html")
