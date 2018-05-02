from django.db import models
from django.urls import reverse

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Zoo Name")
	logoFileName = models.CharField(max_length=200, help_text="Enter Logo File Name", null=True)
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('zooDetail', args=[str(self.id)])
	
class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Exhibit Name")	
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('exhibitDetail', args=[str(self.id)])
		
	def getZooName(self):
		return self.zoo.name

class ExhibitNeighbor(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='fromExhibit')
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='toExhibit')
	
	CARDINAL = (
	    ('n', 'North'),
	    ('s', 'South'),
	    ('e', 'East'),
	    ('w', 'West'),
	    ('nw', 'North West'),
	    ('ne', 'North East'),
	    ('sw', 'South West'),
	    ('se', 'South East'),
	)
	
	direction = models.CharField(max_length=2, choices=CARDINAL, help_text="Enter Direction", null=True, blank=True)
	
	def __str__(self):
		return str(self.fromExhibit) + ': ' + str(self.direction) + ' to: ' + str(self.toExhibit)

class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Animal Name")
	imageFileName = models.CharField(max_length=200, help_text="Enter logo file name", null=True)
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	soundFileName = models.CharField(max_length=200, help_text="Enter sound file name", null=True)
	habitatDescription = models.TextField(max_length=1000, help_text="Enter a description of the Habitat of the animal", null=True)
	dietDescription = models.TextField(max_length=1000, help_text="Enter a description of the Diet of the animal", null=True)
	behaviorDescription = models.TextField(max_length=1000, help_text="Enter a description of the Behavior of the animal", null=True)
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('animalDetail', args=[str(self.id)])
	
	
	
	
	
