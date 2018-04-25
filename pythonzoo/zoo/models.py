from django.db import models

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Zoo Name")
	
	def __str__(self):
		return self.name
	
class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Exhibit Name")	
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name

class ExhibitNeighbors(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	direction = models.CharField(max_length=200)
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name='neighbor_of')
	
	def __str__(self):
		return str(self.fromExhibit) + ': ' + str(self.direction) + ' to: ' + str(self.toExhibit)

class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter Animal Name")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
