from django.db import models

# Create your models here.

class Athlete(models.Model):
    athlete_id = models.CharField(max_length=255, default='0000000')
    name = models.CharField(max_length=255)
    SEX = (
        ('M', 'M'),
        ('F', 'F'),
        )
    age = models.CharField(max_length=5, blank=True, null=True)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    team = models.CharField(max_length=120)
    noc = models.CharField(max_length=3)
    sex = models.CharField(max_length=1, choices=SEX, blank=False, null=False)
    
    def __str__(self):
        return self.name
class Games(models.Model):
    games = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=4)
    SEASON = (
        ("Summer", "Summer"),
        ("Winter", "Winter"),
    )
    season = models.CharField(max_length=6, choices=SEASON, blank=False, null=False)

    def __str__(self):
        return f'{self.year} {self.season}'

class Event(models.Model):
    event = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event}'

class AthleteEvent(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    MEDAL = (
        ("Gold", "Gold"),
        ("Silver", "Silver"),
        ("Bronze", "Bronze"),
        ("NA", "NA"),
    )
    medal = models.CharField(max_length=6, choices=MEDAL, blank=False, null=False)
    def __str__(self):
        return f'{self.athlete} - {self.event}'
        