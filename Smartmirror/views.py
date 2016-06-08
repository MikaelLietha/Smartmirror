# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	return HttpResponse("Tjenare, detta är vanliga index.")

def Test(request):
	return render_to_response("Test.html")