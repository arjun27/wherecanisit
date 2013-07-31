from venues.models import Venue

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render

from django.http import Http404

def index(request):
	latest = Venue.objects.order_by('-pub_date')[:5]
	context = {'latest': latest}
	return render(request, 'venues/index.html', context)

def detail(request, poll_id):
	try:
		venue = Venue.objects.get(pk=poll_id)
	except Venue.DoesNotExist:
		raise Http404
	return render(request, 'venues/detail.html', {'venue': venue})

def results(request, poll_id):
	return HttpResponse("Results of %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("Voting on poll %s." % poll_id)
