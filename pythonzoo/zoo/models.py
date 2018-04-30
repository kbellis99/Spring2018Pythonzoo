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
	
	def get_absolute_url(self):
		return reverse('exhibitDetail', args=[str(self.id)])
		
	def getZooName(self):
		return self.zoo.name

class ExhibitNeighbor(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	direction = models.CharField(max_length=200)
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='neighbor_of')
	
	def __str__(self):
		return str(self.fromExhibit) + ': ' + str(self.direction) + ' to: ' + str(self.toExhibit)

class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Animal Name")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
