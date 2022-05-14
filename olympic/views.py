from logging import raiseExceptions
from django.shortcuts import render
from django.db.models.query import QuerySet

from rest_framework import filters
from rest_framework import serializers, viewsets



from olympic.models import Athlete, Games, Event, AthleteEvent
from olympic.serializers import AthleteSerializer, GamesSerializer, EventSerializer, AthleteEventSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os athelete"""
    queryset = Athlete.objects.all().order_by('name')
    serializer_class = AthleteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','team']
    

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all().order_by('year')
    serializer_class = GamesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['year','season']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('city')
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['event','city']

class AthleteEventViewSet(viewsets.ModelViewSet):
    queryset = AthleteEvent.objects.all().order_by('medal')
    serializer_class = AthleteEventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['athlete','medal']
