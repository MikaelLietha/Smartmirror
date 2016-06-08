# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context,loader

def index(request):
	return HttpResponse("Tjenare, detta är Polls index.")

#def something(request):
#	template = loader.get_template('something.html')
#	return HttpResponse(template.render())

def something(request):
	return render_to_response("something.html")
