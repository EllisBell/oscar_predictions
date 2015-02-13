from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'testmessage': "I am a test message! Roar!"}
	return render(request, 'ktanovsoscar/index.html', context_dict)
