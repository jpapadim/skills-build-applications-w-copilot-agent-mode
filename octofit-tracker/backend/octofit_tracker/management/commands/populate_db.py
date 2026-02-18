from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            # Create users
            users = [
                User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name, is_superhero=True),
                User(name='Iron Man', email='ironman@marvel.com', team=marvel.name, is_superhero=True),
                User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name, is_superhero=True),
                User(name='Batman', email='batman@dc.com', team=dc.name, is_superhero=True),
            ]
            User.objects.bulk_create(users)

            # Create workouts
            workouts = [
                Workout(name='Web Swinging', description='Swing through the city', suggested_for_team='Marvel'),
                Workout(name='Suit Training', description='Train with Iron Man suit', suggested_for_team='Marvel'),
                Workout(name='Amazonian Strength', description='Wonder Woman strength training', suggested_for_team='DC'),
                Workout(name='Batcave Circuit', description='Batman workout routine', suggested_for_team='DC'),
            ]
            Workout.objects.bulk_create(workouts)

            # Create activities
            spiderman = User.objects.get(email='spiderman@marvel.com')
            batman = User.objects.get(email='batman@dc.com')
            Activity.objects.create(user=spiderman, type='Cardio', duration=30, date='2024-01-01')
            Activity.objects.create(user=batman, type='Strength', duration=45, date='2024-01-02')

            # Create leaderboard
            Leaderboard.objects.create(team=marvel, points=100)
            Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
