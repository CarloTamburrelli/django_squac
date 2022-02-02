from django.shortcuts import render
from system.models import SystemGame
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
	return render(request, 'system/home.html')

def About(request):
	return render(request, 'system/about.html', { 'title' : 'About'})

@login_required
def Fight(request, id):

	try:
		fight = SystemGame.objects.get(~Q(user2_id = None), id=id)
	except SystemGame.DoesNotExist:
		raise Http404("Game not found.")

	return render(request, 'system/fight.html', { 'fight' : fight })