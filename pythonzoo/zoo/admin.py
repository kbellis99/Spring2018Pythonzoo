from django.contrib import admin
from .models import Zoo, Exhibit, ExhibitNeighbor, Animal


# Register your models here.

class ZooAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'zoo')


admin.site.register(Exhibit, ExhibitAdmin)

class ExhibitNeighborAdmin(admin.ModelAdmin):
	list_display = ('fromExhibit', 'direction', 'toExhibit')

admin.site.register(ExhibitNeighbor, ExhibitNeighborAdmin)

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'exhibit')


admin.site.register(Animal, AnimalAdmin)
