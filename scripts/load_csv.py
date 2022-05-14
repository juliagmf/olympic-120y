from olympic.models import Athlete, Games, Event, AthleteEvent
import csv



def run():
    with open('olympic/athlete_events.csv') as file:
        reader = csv.reader(file)
        next(reader)  

        Athlete.objects.all().delete()
        Games.objects.all().delete()
        Event.objects.all().delete()
        AthleteEvent.objects.all().delete()

        for row in reader:
            print(row)

            athlete, _ = Athlete.objects.get_or_create(
                        athlete_id=row[0],
                        name=row[1],
                        sex=row[2],
                        age=row[3],
                        height=row[4],
                        weight=row[5],
                        team=row[6],
                        noc=row[7],
                       )
            games, _ = Games.objects.get_or_create(
                        games=row[8],
                        year=row[9],
                        season=row[10],
                       )

            event, _ = Event.objects.get_or_create(
                        city=row[11],
                        sport=row[12],
                        event=row[13],
                        games=games,
                       )
            athlete_event, _ = AthleteEvent.objects.get_or_create(
                        athlete=athlete,
                        games=games,
                        event=event,
                        medal=row[14],
                       )

            athlete.save()
            games.save()
            event.save()
            athlete_event.save()
