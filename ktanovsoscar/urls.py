from django.conf.urls import patterns, url
from ktanovsoscar import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))