from django.db import models
from django.db.models import fields
from rest_framework import serializers
from olympic.models import Athlete, Games, Event, AthleteEvent

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['athlete_id', 'name', 'sex', 'age', 'height', 'weight', 'team','noc']

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['games','year', 'season']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event', 'city', 'sport', 'games']

class AthleteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteEvent
        fields = ['athlete', 'games','event','medal']

    