import json
from django.conf import settings
import os
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data from test_data.json'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Load test data from JSON
        test_data_path = os.path.join(settings.BASE_DIR, 'octofit_tracker', 'test_data.json')
        with open(test_data_path, 'r') as f:
            data = json.load(f)

        # Create users
        email_to_user = {}
        for u in data['users']:
            user = User.objects.create(username=u['username'], email=u['email'], password=u['password'])
            email_to_user[u['email']] = user

        # Create teams
        for t in data['teams']:
            team = Team.objects.create(name=t['name'])
            members = [email_to_user[email] for email in t['members'] if email in email_to_user]
            team.members.set(members)

        # Create activities
        for a in data['activity']:
            user = email_to_user.get(a['user'])
            if user:
                Activity.objects.create(user=user, activity_type=a['activity_type'], duration=f"00:{a['duration']:02}:00")

        # Create leaderboard
        for l in data['leaderboard']:
            user = email_to_user.get(l['user'])
            if user:
                Leaderboard.objects.create(user=user, score=l['score'])

        # Create workouts
        for w in data['workouts']:
            Workout.objects.create(name=w['name'], description=w['description'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data from test_data.json'))
