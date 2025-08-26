from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test', first_name='Clark', last_name='Kent'),
        ]

        # Activities
        Activity.objects.create(name='Run', user='ironman', team='Marvel')
        Activity.objects.create(name='Swim', user='spiderman', team='Marvel')
        Activity.objects.create(name='Fly', user='superman', team='DC')
        Activity.objects.create(name='Martial Arts', user='batman', team='DC')

        # Leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='spiderman', team='Marvel', score=90)
        Leaderboard.objects.create(user='batman', team='DC', score=95)
        Leaderboard.objects.create(user='superman', team='DC', score=98)

        # Workouts
        Workout.objects.create(name='Chest Day', description='Bench press and pushups', user='ironman')
        Workout.objects.create(name='Web Slinging', description='Agility and cardio', user='spiderman')
        Workout.objects.create(name='Gadget Training', description='Tech and combat', user='batman')
        Workout.objects.create(name='Flight Training', description='Aerial maneuvers', user='superman')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
