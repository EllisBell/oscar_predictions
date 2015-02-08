from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("this is going to be an oscar predictions website </br> stay tuned...")
