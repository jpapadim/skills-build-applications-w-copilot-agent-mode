from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel', is_superhero=True)
        self.assertEqual(user.name, 'Test')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test', email='test2@example.com', team='Marvel', is_superhero=True)
        activity = Activity.objects.create(user=user, type='Cardio', duration=20, date='2024-01-01')
        self.assertEqual(activity.type, 'Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team2', description='Desc2')
        leaderboard = Leaderboard.objects.create(team=team, points=10)
        self.assertEqual(leaderboard.points, 10)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc', suggested_for_team='Marvel')
        self.assertEqual(workout.name, 'Test Workout')
