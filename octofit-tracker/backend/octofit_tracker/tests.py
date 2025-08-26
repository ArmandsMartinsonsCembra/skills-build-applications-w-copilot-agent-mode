from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_activity(self):
        activity = Activity.objects.create(name='Test', user='user', team='team')
        self.assertEqual(str(activity), 'Test - user')

    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='user', team='team', score=10)
        self.assertEqual(str(lb), 'user - 10')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test', description='desc', user='user')
        self.assertEqual(str(workout), 'Test - user')
