from django.shortcuts import render
from django.views import generic
from .models import Zoo, Exhibit, Animal

# Create your views here.

def aboutUs(request):
	return render(
		request,
		'zoo/aboutUs.html',
		context = { },
	)

class ZooListView(generic.ListView):
	model = Zoo

class zooDetailView(generic.DetailView):
	model = Zoo

class ExhibitDetailView(generic.DetailView):
	model = Exhibit

class AnimalDetailView(generic.DetailView):
	model = Animal
