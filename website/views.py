from django.shortcuts import render
from django.http import HttpResponse
import json





# Create your views here.
def brewer_post(request):
	#unico = request.body.decode('utf-8')
	#data = json.loads(unico)
	if request.method == 'POST':
		return
	elif request.method == 'GET':
		print "body" + request.body
		#get query from the request:
		s = request.META['QUERY_STRING']
		
		return HttpResponse("mjau")

	#return HttpResponse("mjau")
		
