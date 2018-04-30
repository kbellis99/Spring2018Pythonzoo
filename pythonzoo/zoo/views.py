from django.shortcuts import render
from django.views import generic
from .models import Zoo, Exhibit

# Create your views here.

def index(request):
	temporaryData = 'Kristen'
	return render(
		request,
		'index.html',
		context = {'temporaryData' : temporaryData},
	)

class zooDetailView(generic.DetailView):
	model = Zoo

class exhibitDetailView(generic.DetailView):
	model = Exhibit
