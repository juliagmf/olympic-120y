# 120 years of Olympic history: athletes and results
API rest para servir os dados do dataset “120 years of Olympic history: athletes and results”
### Atualizando o sistema
```
sudo apt update 
sudo apt -y upgrade
```
### Instalando o Python3
```
sudo apt install python3-pip
```
### Instalando o env e virtualenv
```
sudo apt install -y python3-venv
```
```
sudo apt install python3-virtualenv
```
### Criando o ambiente virtual
```
virtualenv env -p python3
```
### Ativando o ambiente virtual
```
. env/bin/activate
```
### Instalando o Django
```
pip install django
```
### Criando o projeto
```
django-admin startproject core .
```
### Instalando o Django Rest Framework
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
### django-extensions 
```
pip install django django-extensions pandas plotly
```

### Criando uma aplicação
```
python manage.py startapp olympic
```
### Dizendo ao Django para usar a aplicação 
abra o arquivo core/settings.py
```
Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #framework
    'olympic', #app
    'django_extensions', # add extensão
]
```
### Criando os modelos
abra o arquivo olympic/models.py 
```
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
```
### Criando um banco de dados
```
python3 manage.py migrate
```

### Criando tabelas para os modelos no banco de dados
```
python3 manage.py makemigrations olympic
```
#### Aplicando ao banco de dados
```
python3 manage.py migrate olympic
```
### Adicionando o arquivo csv
adicione o arquivo csv em olympic/athelete_events.csv

### Script
crie uma pasta de scripts na raiz do projeto
```
mkdir scripts
```
crie o arquivo scripts/load_csv.py

### Open csv
scripts/load_csv.py
```
```
Executando o arquivo
```
python manage.py runscript load_csv
```
espere... são 271116 linhas!

### Django Admin
abra o arquivo olympic/admin.py
```
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

```
### Serialização
Crie um arquivo no diretório olympic denominado serializers.py (olympic/serializer.py) e adicione o seguinte código.
```
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

    
```
### Views
Edite o arquivo olympic/views.py e adicione o seguinte:

```
from olympic.models import Athlete, Games, Event, AthleteEvent
from olympic.serializer import AthleteSerializer, GamesSerializer, EventSerializer, AthleteEventSerializer


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

```

### URLs
abra o arquivo core/urls.py
```
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from olympic.views import AthleteViewSet, GamesViewSet, EventViewSet, AthleteEventViewSet

router = routers.DefaultRouter()
router.register('athlete', AthleteViewSet, basename='Athlete')
router.register('games', GamesViewSet, basename='Games')
router.register('event', EventViewSet, basename='Event')
router.register('athlete_event', AthleteEventViewSet, basename='AthleteEvent')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

]

```
### Startando o servidor
```
python3 manage.py runserver
```
### ...
