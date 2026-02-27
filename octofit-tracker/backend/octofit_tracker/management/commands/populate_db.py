from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='cap@marvel.com', name='Captain America', team='Marvel'),
            User(email='thor@marvel.com', name='Thor', team='Marvel'),
            User(email='hulk@marvel.com', name='Hulk', team='Marvel'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
            User(email='flash@dc.com', name='Flash', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30),
            Activity(user='Captain America', activity_type='Cycling', duration=45),
            Activity(user='Thor', activity_type='Swimming', duration=60),
            Activity(user='Hulk', activity_type='Weightlifting', duration=50),
            Activity(user='Superman', activity_type='Flying', duration=120),
            Activity(user='Batman', activity_type='Martial Arts', duration=40),
            Activity(user='Wonder Woman', activity_type='Archery', duration=35),
            Activity(user='Flash', activity_type='Sprinting', duration=20),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=185)
        Leaderboard.objects.create(team='DC', points=215)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes.', difficulty='Hard'),
            Workout(name='Power Yoga', description='Yoga for strength and flexibility.', difficulty='Medium'),
            Workout(name='Speed Run', description='Running workout for speed.', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
