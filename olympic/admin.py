from django.contrib import admin
from olympic.models import Athlete, Games, Event, AthleteEvent
# Register your models here.

class Athletes(admin.ModelAdmin):
    list_display = ('athlete_id', 'name', 'sex', 'age', 'height', 'weight', 'team', 'noc')
    search_fields = ('name',)

admin.site.register(Athlete, Athletes)

class Game(admin.ModelAdmin):
    list_display = ('games','year', 'season')
    search_fields = ('year',)

admin.site.register(Games, Game)

class Events(admin.ModelAdmin):
    list_display = ('event', 'city', 'sport', 'games')
    search_fields = ('event',)

admin.site.register(Event, Events)

class AthleteEvents(admin.ModelAdmin):
    list_display = ('athlete', 'games','event','medal')
    search_fields = ('medal',)

admin.site.register(AthleteEvent, AthleteEvents)
