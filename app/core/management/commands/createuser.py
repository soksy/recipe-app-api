# filepath: app/core/management/commands/createuser.py
from django.core.management.base import BaseCommand
from core.models import User

class Command(BaseCommand):
    help = 'Create a regular user'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address of the user')
        parser.add_argument('password', type=str, help='Password for the user')
        parser.add_argument('--name', type=str, default='', help='Name of the user')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        name = kwargs['name']

        user = User.objects.create_user(email=email, password=password, name=name)
        self.stdout.write(self.style.SUCCESS(f"User created: {user.email}"))